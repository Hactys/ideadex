from typing import List
from ideadex.data import load_cards, save_relation
from ideadex.domain.card import Card
from ideadex.domain.relation import Relation


def display_card(card: Card) -> None:
    """Affiche une carte dans la console."""
    print("\n" + "-" * 40)
    print(card.title.upper())
    print(card.description)
    print(f"Thèmes : {', '.join(card.themes)}")
    print("-" * 40)


def ask_user_action() -> str:
    """
    Demande une action à l'utilisateur.
    Retourne : 'like', 'oppose', 'pass', ou 'quit'
    """
    print("[1] Like")
    print("[2] Dislike")
    print("[3] Passer")
    print("[q] Quitter")

    while True:
        choice = input("Votre choix : ").strip().lower()
        if choice == "1":
            return "like"
        elif choice == "2":
            return "oppose"
        elif choice == "3":
            return "pass"
        elif choice == "q":
            return "quit"
        else:
            print("Entrée invalide, veuillez réessayer.")


def run_cli(cards: List[Card]) -> None:
    """
    Boucle principale de la CLI.
    """
    print("Bienvenue dans IdeaDex 🧠")
    print("Explorez des idées et réagissez librement.\n")
    for card in cards:
        display_card(card)
        action = ask_user_action()
        if action == "quit":
            print("\nFin de session. Merci !")
            break
        if action in {"like", "oppose"}:
            relation = Relation(
                from_card=card.id,
                to_card=card.id,
                kind=action,
            )
            save_relation(relation)
            print(f"Action enregistrée : {action}")
        else:
            print("Carte passée.")
    return


def main():
    cards = load_cards()
    run_cli(cards)


if __name__ == "__main__":
    main()
