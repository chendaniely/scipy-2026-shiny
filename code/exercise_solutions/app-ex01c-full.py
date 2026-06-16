from palmerpenguins import load_penguins
from plotnine import aes, geom_point, ggplot, theme_minimal
from shiny import reactive  #<<
from shiny.express import input, render, ui

dat = load_penguins().dropna()
num_cols = dat.select_dtypes("float64").columns.tolist()
species = dat["species"].unique().tolist()

ui.input_select("x", "", num_cols, selected="bill_depth_mm")
ui.input_select("y", "", num_cols, selected="body_mass_g")
ui.input_checkbox_group("species", "Species", species, selected=species)


@reactive.calc  #<<
def filtered():  #<<
    return dat[dat["species"].isin(input.species())]  #<<


@render.plot
def plot():
    return (
        ggplot(filtered(), aes(x=input.x(), y=input.y(), color="species"))  #<<
        + geom_point(alpha=0.7)
        + theme_minimal()
    )


@render.text  #<<
def count():  #<<
    return f"{len(filtered())} penguins selected"  #<<
