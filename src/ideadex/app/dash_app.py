import dash_bootstrap_components as dbc
from dash import Dash, callback_context, html, dcc, callback, Output, Input, ALL, State

from ideadex.app.components import make_card
from ideadex.data import load_cards, save_relation
from ideadex.domain import card
from ideadex.domain.card import Card
from ideadex.domain.relation import Relation


app = Dash("Ideadex", external_stylesheets=[dbc.themes.BOOTSTRAP])
cards_data = load_cards()


app.layout = [
    html.H1(children="Ideadex", style={"textAlign": "center"}),
    dbc.Container(
        [
            dcc.Store(id="active-index", data=0),
            html.Div(
                [make_card(card) for card in cards_data],
                id="carousel-container",
                className="carousel-container",
            ),
            dbc.ButtonGroup(
                [
                    dbc.Button("◀", id="prev", n_clicks=0),
                    dbc.Button("▶", id="next", n_clicks=0),
                ],
                className="mt-4",
            ),
        ],
        fluid=True,
    ),
]


@app.callback(
    Output("active-index", "data"),
    Input("prev", "n_clicks"),
    Input("next", "n_clicks"),
    State("active-index", "data"),
)
def update_index(prev, next_, index):
    print(prev, next_, index)
    ctx = callback_context
    if not ctx.triggered:
        return index

    btn = ctx.triggered[0]["prop_id"].split(".")[0]
    if btn == "prev":
        return (index - 1) % len(cards_data)
    else:
        return (index + 1) % len(cards_data)


@app.callback(
    Output({"type": "card-wrapper", "index": ALL}, "className"),
    Input("active-index", "data"),
)
def update_classes(active):
    classes = []
    for i in range(len(cards_data)):
        if i == active:
            classes.append("card-wrapper active")
        elif i == (active - 1) % len(cards_data):
            classes.append("card-wrapper prev")
        elif i == (active + 1) % len(cards_data):
            classes.append("card-wrapper next")
        else:
            classes.append("card-wrapper hidden")
    return classes


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
