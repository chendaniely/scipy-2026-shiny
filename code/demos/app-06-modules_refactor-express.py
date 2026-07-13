"""Tips dashboard, Express syntax, filter sidebar extracted into a module."""

import seaborn as sns
from shiny.express import render, ui

from filter_module_express import filter_panel

tips = sns.load_dataset("tips")

ui.page_opts(title="Restaurant tipping", fillable=True)

with ui.sidebar():
    tips_filter = filter_panel(
        "tips_filter", data=tips, columns=["total_bill", "time"]
    )

with ui.card():
    ui.card_header("Filtered tips")

    @render.data_frame
    def tips_table():
        return tips.loc[tips_filter["mask"]()]
