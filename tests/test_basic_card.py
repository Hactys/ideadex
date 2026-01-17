import pytest

from ideadex.domain.card import Card


def test_card_creation():
    card = Card(1, "Test", "Desc", ["A"])
    assert card.id == 1
