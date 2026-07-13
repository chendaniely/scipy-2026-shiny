"""Two datasets, two tabs, one reused filter module (Core syntax)."""

import seaborn as sns
from palmerpenguins import load_penguins
from shiny import App, render, ui

from filter_module_core import filter_server, filter_ui

tips = sns.load_dataset("tips")
penguins = load_penguins().dropna()

app_ui = ui.page_fillable(
    ui.navset_card_tab(
        ui.nav_panel(
            "Tips",
            ui.layout_sidebar(
                ui.sidebar(filter_ui("tips_filter")),
                ui.output_data_frame("tips_table"),
            ),
        ),
        ui.nav_panel(
            "Penguins",
            ui.layout_sidebar(
                ui.sidebar(filter_ui("penguins_filter")),
                ui.output_data_frame("penguins_table"),
            ),
        ),
    ),
)


def server(input, output, session):
    tips_filter = filter_server(
        "tips_filter", data=tips, columns=["total_bill", "time"]
    )

    @render.data_frame
    def tips_table():
        return tips.loc[tips_filter["mask"]()]

    penguins_filter = filter_server(
        "penguins_filter",
        data=penguins,
        columns=["species", "bill_length_mm", "body_mass_g"],
    )

    @render.data_frame
    def penguins_table():
        return penguins.loc[penguins_filter["mask"]()]


app = App(app_ui, server)
