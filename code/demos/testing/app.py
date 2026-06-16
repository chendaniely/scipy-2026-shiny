from palmerpenguins import load_penguins
from shiny.express import input, render, ui

dat = load_penguins().dropna()

ui.input_radio_buttons("species", "Species", ["Adelie", "Chinstrap", "Gentoo"])

with ui.card():
    @render.text
    def n_rows():
        filtered = dat[dat["species"] == input.species()]
        return f"{len(filtered)} penguins"
