from shiny.express import render, ui
from querychat.express import QueryChat
from querychat.data import titanic


# 1. Provide data source to QueryChat
qc = QueryChat(titanic(), "titanic", client="github/gpt-4.1")

# 2. Add sidebar chat control
qc.sidebar()

# 3. Add a card with reactive title and data frame
with ui.card():
    with ui.card_header():
        @render.text
        def title():
            return qc.title() or "Titanic Dataset"

    @render.text
    def query():
        return qc.sql()

    @render.data_frame
    def data_table():
        return qc.df()
