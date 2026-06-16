from pathlib import Path

from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import run_shiny_app

APP = Path(__file__).parent / "app.py"


def test_default_state(page: Page):
    with run_shiny_app(str(APP)) as app:
        page.goto(app.url)

        radio = controller.InputRadioButtons(page, "species")
        radio.expect_selected("Adelie")
        radio.expect_choices(["Adelie", "Chinstrap", "Gentoo"])


def test_species_filter(page: Page):
    with run_shiny_app(str(APP)) as app:
        page.goto(app.url)

        radio = controller.InputRadioButtons(page, "species")
        text = controller.OutputText(page, "n_rows")

        radio.set("Chinstrap")
        text.expect_value("68 penguins")
