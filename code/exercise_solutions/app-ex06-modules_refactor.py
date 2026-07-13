"""Exercise 6 solution: tips dashboard with filter sidebar as a module,
including the reset button the slides' version dropped."""

import seaborn as sns
from shiny import reactive
from shiny.express import input, render, ui

from module import filter_panel

tips = sns.load_dataset("tips")

ui.page_opts(title="Restaurant tipping", fillable=True)

with ui.sidebar():
    tips_filter = filter_panel(
        "tips_filter", data=tips, columns=["total_bill", "time"]
    )
    ui.input_action_button("action_button", "Reset filter")


@reactive.effect
@reactive.event(input.action_button)
def reset_filters():
    ui.update_slider(
        "tips_filter-filter_total_bill",
        value=[tips.total_bill.min(), tips.total_bill.max()],
    )
    ui.update_checkbox_group(
        "tips_filter-filter_time",
        selected=["Lunch", "Dinner"],
    )


with ui.card():
    ui.card_header("Filtered tips")

    @render.data_frame
    def tips_table():
        return tips.loc[tips_filter["mask"]()]
