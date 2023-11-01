
from dataclasses import dataclass


@dataclass
class BaseEntity:
    HP: int
    Att: int
    Def: int
    