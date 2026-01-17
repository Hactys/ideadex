from src.ideadex.domain import Card, Relation

# TODO : V <- compléter ces fonctions pour load des cartes et sauvegarder des relations
# Il faudra utiliser json dans un premier temps puis on passera en mode DB
# Ton but est de faire une interface pour rendre le code agnostique de l'implémentation.


def load_cards() -> list[Card]: ...


def save_relation(relation: Relation) -> None: ...
