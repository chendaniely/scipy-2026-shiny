from shiny.express import input, render, ui

ui.page_opts(title="Tips Dashboard", fillable=True)

with ui.sidebar():
    ui.input_slider("bill", "Max bill ($)", 3, 50, 25)
    ui.input_checkbox_group(
        "time",
        "Meal",
        ["Lunch", "Dinner"],
        selected=["Lunch", "Dinner"],
    )
    ui.input_action_button("action_button", "Reset")

with ui.layout_columns():
    with ui.card():
        ...  # output 1

    with ui.card():
        ...  # output 2

    with ui.card():
            ...  # output 3

with ui.layout_columns():
    with ui.card():
        ...  # data frame

    with ui.card():
        ...  # scatter plot

with ui.layout_columns():
    with ui.card():
        ...  # ridgeplot