import altair as alt
import seaborn as sns
from shiny.express import input, ui, render
from shiny import reactive
from shinywidgets import render_altair, render_widget

tips = sns.load_dataset("tips")

# title
ui.page_opts(title="Restaurant tipping", fillable=True)

# sidebar
with ui.sidebar(open="desktop"):
    ui.input_slider(
        id="slider",
        label="Bill amount",
        min=tips.total_bill.min(),
        max=tips.total_bill.max(),
        value=[tips.total_bill.min(), tips.total_bill.max()],
    )
    ui.input_checkbox_group(
        id="checkbox_group",
        label="Food service",
        choices={
            "Lunch": "Lunch",
            "Dinner": "Dinner",
        },
        selected=[
            "Lunch",
            "Dinner",
        ],
    )

@reactive.calc
def filtered_data():
    idx1 = tips.total_bill.between(
        left=input.slider()[0],
        right=input.slider()[1],
        inclusive="both",
    )
    idx2 = tips.time.isin(input.checkbox_group())
    tips_filtered = tips[idx1 & idx2]
    return tips_filtered


# body of application
# first row of value boxes
with ui.layout_columns(fill=False):
    with ui.value_box():
        "Total tippers"

        @render.text
        def total_tippers():
            return filtered_data().shape[0]

    with ui.value_box():
        "Average tip"

        @render.text
        def average_tip():
            perc = filtered_data().tip / filtered_data().total_bill
            return f"{perc.mean():.1%}"

    with ui.value_box():
        "Average bill"

        @render.text
        def average_bill():
            bill = filtered_data().total_bill.mean()
            return f"${bill:.2f}"


# second row of cards
with ui.layout_columns(col_widths=[6, 6]):
    with ui.card(full_screen=True):
        ui.card_header("Tips data")

        @render.data_frame
        def tips_data():
            return filtered_data()

    with ui.card(full_screen=True):
        ui.card_header("Total bill vs tip")

        @render_altair
        def scatterplot():
            data = filtered_data()
            points = alt.Chart(data).mark_circle().encode(
                x=alt.X("total_bill", title="Total bill"),
                y=alt.Y("tip", title="Tip"),
                tooltip=[
                    alt.Tooltip("total_bill:Q", title="Total bill", format=".2f"),
                    alt.Tooltip("tip:Q", title="Tip", format=".2f"),
                ],
            )
            trend = points.transform_regression(
                "total_bill", "tip", method="linear"
            ).mark_line()
            zoom = alt.selection_interval(bind="scales")
            return (points + trend).add_params(zoom).properties(width="container")
