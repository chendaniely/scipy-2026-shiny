"""Two datasets, two tabs, one reused filter module (Express syntax)."""

import seaborn as sns
from palmerpenguins import load_penguins
from shiny.express import render, ui

from filter_module_express import filter_panel

tips = sns.load_dataset("tips")
penguins = load_penguins().dropna()

ui.page_opts(fillable=True)

with ui.navset_card_tab():
    with ui.nav_panel("Tips"):
        with ui.layout_sidebar():
            with ui.sidebar():
                tips_filter = filter_panel(
                    "tips_filter", data=tips, columns=["total_bill", "time"]
                )

            @render.data_frame
            def tips_table():
                return tips.loc[tips_filter["mask"]()]

    with ui.nav_panel("Penguins"):
        with ui.layout_sidebar():
            with ui.sidebar():
                penguins_filter = filter_panel(
                    "penguins_filter",
                    data=penguins,
                    columns=["species", "bill_length_mm", "body_mass_g"],
                )

            @render.data_frame
            def penguins_table():
                return penguins.loc[penguins_filter["mask"]()]
