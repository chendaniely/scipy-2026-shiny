"""Reusable Shiny Express module: same behavior as filter_module_core.py,
using the Express `@module` decorator (one function is both UI and server)."""

import pandas as pd
from shiny import reactive
from shiny.express import module, render, ui


def _make_filters(data, columns):
    filters = {}
    for col in columns:
        if pd.api.types.is_numeric_dtype(data[col]):
            lo, hi = float(data[col].min()), float(data[col].max())
            filters[col] = {
                "kind": "range",
                "component": ui.input_slider(
                    f"filter_{col}",
                    f"Range for {col}",
                    min=lo,
                    max=hi,
                    value=[lo, hi],
                ),
            }
        else:
            choices = sorted(data[col].unique())
            filters[col] = {
                "kind": "isin",
                "component": ui.input_checkbox_group(
                    f"filter_{col}",
                    f"Select {col}",
                    choices=choices,
                    selected=choices,
                ),
            }
    return filters


@module
def filter_panel(input, output, session, data, columns):
    ui_filters = _make_filters(data, columns)

    @render.ui
    def filters():
        return [ui_filters[col]["component"] for col in columns]

    @reactive.calc
    def mask():
        m = pd.Series(True, index=data.index)
        for col in columns:
            if ui_filters[col]["kind"] == "range":
                lo, hi = input[f"filter_{col}"]()
                m = m & data[col].between(lo, hi)
            else:
                m = m & data[col].isin(input[f"filter_{col}"]())
        return m

    return {"mask": mask}
