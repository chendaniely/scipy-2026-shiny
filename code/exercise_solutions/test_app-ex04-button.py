from pathlib import Path

import seaborn as sns
from playwright.sync_api import Page
from shiny.playwright import controller
from shiny.run import run_shiny_app

APP = Path(__file__).parent / "app-ex04-button.py"
tips = sns.load_dataset("tips")


def test_default_state(page: Page):
    with run_shiny_app(str(APP)) as app:
        page.goto(app.url)

        checkbox_group = controller.InputCheckboxGroup(page, "checkbox_group")
        total_tippers = controller.OutputText(page, "total_tippers")

        checkbox_group.expect_selected(["Lunch", "Dinner"])
        total_tippers.expect_value(str(tips.shape[0]))


def test_checkbox_filter(page: Page):
    with run_shiny_app(str(APP)) as app:
        page.goto(app.url)

        checkbox_group = controller.InputCheckboxGroup(page, "checkbox_group")
        total_tippers = controller.OutputText(page, "total_tippers")

        checkbox_group.set(["Dinner"])

        expected = tips[tips["time"] == "Dinner"].shape[0]
        total_tippers.expect_value(str(expected))


def test_reset_button(page: Page):
    with run_shiny_app(str(APP)) as app:
        page.goto(app.url)

        checkbox_group = controller.InputCheckboxGroup(page, "checkbox_group")
        action_button = controller.InputActionButton(page, "action_button")
        total_tippers = controller.OutputText(page, "total_tippers")

        checkbox_group.set(["Dinner"])
        action_button.click()

        checkbox_group.expect_selected(["Lunch", "Dinner"])
        total_tippers.expect_value(str(tips.shape[0]))
