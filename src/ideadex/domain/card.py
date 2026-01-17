from dataclasses import dataclass
from typing import List


@dataclass
class Card:
    id: int
    title: str
    description: str
    themes: List[str]
    # TODO : V <- complète ce qu'il te semble le plus intéressant de mettre ici
