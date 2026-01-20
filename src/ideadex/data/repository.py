import json
from ideadex.domain import Card, Relation


# TODO : V <- compléter ces fonctions pour load des cartes et sauvegarder des relations
# Il faudra utiliser json dans un premier temps puis on passera en mode DB
# Ton but est de faire une interface pour rendre le code agnostique de l'implémentation.


def load_cards() -> list[Card]:
    """Lit le document json pour avoir une liste de carte exploitable"""
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
    """Enregistre dans un fichier json les relations entre les cartes"""
    relation_to_save = {
        "from_card": relation.from_card,
        "to_card": relation.to_card,
        "kind": relation.kind,
    }
    try:
        with open("relations.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    if relation_to_save not in data:
        data.append(relation_to_save)
    with open("relations.json", "w") as file:
        json.dump(data, file)
