from itertools import combinations

from palmerpenguins import load_penguins
from plotnine import aes, geom_bin2d, geom_point, ggplot, theme_minimal
from shiny.express import module, render, ui

dat = load_penguins().dropna()
num_cols = dat.select_dtypes("float64").columns.tolist()


@module
def scatter_panel(input, output, session, data, x, y):
    ui.input_radio_buttons("view", None, choices=["Points", "Density"], inline=True)

    @render.plot
    def plot():
        p = ggplot(data, aes(x=x, y=y)) + theme_minimal()
        if input.view() == "Points":
            p = p + geom_point(aes(color="species"), alpha=0.6)
        else:
            p = p + geom_bin2d(bins=20)
        return p


ui.page_opts(title="Scatterplot combinations", fillable=True)

with ui.layout_columns(col_widths=6):
    for x, y in combinations(num_cols, 2):
        with ui.card():
            ui.card_header(f"{x} vs {y}")
            scatter_panel(f"{x}_{y}", data=dat, x=x, y=y)
