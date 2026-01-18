import json
from ideadex.domain import Card, Relation


# TODO : V <- compléter ces fonctions pour load des cartes et sauvegarder des relations
# Il faudra utiliser json dans un premier temps puis on passera en mode DB
# Ton but est de faire une interface pour rendre le code agnostique de l'implémentation.


def load_cards() -> list[Card]:
    with open("cards.json", "r") as file:
        data = json.load(file)
    liste = []
    for dic in data:
        liste.append(
            Card(
                id=dic["id"],
                title=dic["title"],
                description=dic["description"],
                themes=dic["themes"],
            )
        )
    return liste


def save_relation(relation: Relation) -> None:
    ...
