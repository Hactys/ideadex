from ideadex.data.repository import load_cards, save_relation
from ideadex.domain import Relation


def main():
    print("Hello from CLI")
    print(load_cards())
    r = Relation(1, 1, "like")
    save_relation(r)


if __name__ == "__main__":
    main()
