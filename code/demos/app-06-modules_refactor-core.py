"""Tips dashboard, Core syntax, filter sidebar extracted into a module."""

import seaborn as sns
from shiny import App, render, ui

from filter_module_core import filter_server, filter_ui

tips = sns.load_dataset("tips")

app_ui = ui.page_sidebar(
    ui.sidebar(filter_ui("tips_filter")),
    ui.card(
        ui.card_header("Filtered tips"),
        ui.output_data_frame("tips_table"),
    ),
    title="Restaurant tipping",
)


def server(input, output, session):
    tips_filter = filter_server(
        "tips_filter", data=tips, columns=["total_bill", "time"]
    )

    @render.data_frame
    def tips_table():
        return tips.loc[tips_filter["mask"]()]


app = App(app_ui, server)
