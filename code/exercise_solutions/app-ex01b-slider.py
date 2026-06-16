from palmerpenguins import load_penguins
from plotnine import aes, geom_point, ggplot, theme_minimal
from shiny.express import input, render, ui

dat = load_penguins().dropna()
num_cols = dat.select_dtypes("float64").columns.tolist()

ui.input_select("x", "", num_cols, selected="bill_depth_mm")
ui.input_select("y", "", num_cols, selected="body_mass_g")
ui.input_slider(  #<<
    "body_mass", "Body Mass (g)",  #<<
    min=int(dat["body_mass_g"].min()),  #<<
    max=int(dat["body_mass_g"].max()),  #<<
    value=[int(dat["body_mass_g"].min()), int(dat["body_mass_g"].max())],  #<<
)  #<<


@render.plot
def plot():
    sel = dat[  #<<
        (dat["body_mass_g"] >= input.body_mass()[0])  #<<
        & (dat["body_mass_g"] <= input.body_mass()[1])  #<<
    ]  #<<
    return (
        ggplot(sel, aes(x=input.x(), y=input.y(), color="species"))  #<<
        + geom_point(alpha=0.7)
        + theme_minimal()
    )
