from dataclasses import dataclass, field

@dataclass(frozen=True)
class Class:
    attack_mod: float = field()
    defense_mod: float = field()

    def __str__(self) -> str:
        pass

@dataclass(frozen=True)
class Warrior(Class):
    attack_mod: float = 0.6
    defense_mod: float = 0.4

    def __str__(self):
        return f"Warrior"

@dataclass(frozen=True)
class Archer(Class):
    attack_mod: float = 0.9
    defense_mod: float = 0.1

    def __str__(self):
        return f"Archer"

@dataclass(frozen=True)
class Defender(Class):
    attack_mod: float = 0.1
    defense_mod: float = 0.9

    def __str__(self):
        return f"Defender"


@dataclass(frozen=True)
class Infiltrator(Class):
    attack_mod: float = 0.8
    defense_mod: float = 0.3

    def __str__(self):
        return f"Infiltrator"
