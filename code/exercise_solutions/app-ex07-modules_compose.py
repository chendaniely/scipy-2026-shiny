"""Exercise 7 solution: Exercise 6's tips app, plus a Penguins tab reusing
the same filter module."""

import seaborn as sns
from palmerpenguins import load_penguins
from shiny import reactive
from shiny.express import input, render, ui

from module import filter_panel

tips = sns.load_dataset("tips")
penguins = load_penguins().dropna()

ui.page_opts(title="Restaurant tipping + Penguins", fillable=True)

with ui.navset_card_tab():
    with ui.nav_panel("Tips"):
        with ui.layout_sidebar():
            with ui.sidebar():
                tips_filter = filter_panel(
                    "tips_filter", data=tips, columns=["total_bill", "time"]
                )
                ui.input_action_button("reset_tips", "Reset filter")

            @reactive.effect
            @reactive.event(input.reset_tips)
            def reset_tips_filters():
                ui.update_slider(
                    "tips_filter-filter_total_bill",
                    value=[tips.total_bill.min(), tips.total_bill.max()],
                )
                ui.update_checkbox_group(
                    "tips_filter-filter_time",
                    selected=["Lunch", "Dinner"],
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
