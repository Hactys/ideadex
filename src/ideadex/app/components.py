import dash_bootstrap_components as dbc
from dash import html

from ideadex.domain.card import Card


def make_card(card: Card):
    return html.Div(
        dbc.Card(
            [
                dbc.CardHeader(card.title),
                dbc.CardBody(
                    [
                        html.P(card.description, className="card-text"),
                        html.Div(
                            [
                                dbc.Badge(theme, color="primary", className="me-1")
                                for theme in card.themes
                            ]
                        ),
                    ]
                ),
            ],
            className="carousel-card",
        ),
        id={"type": "card-wrapper", "index": card.id},
        className="card-wrapper",
    )
