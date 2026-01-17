from dataclasses import dataclass


@dataclass
class Relation:
    from_card: int
    to_card: int
    kind: str  # "like", "oppose", "link"
