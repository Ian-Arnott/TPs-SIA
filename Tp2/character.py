import random
import math


class Character(object):
    _stats: dict[str, float] = {"strength": 0, "agility": 0, "expertise": 0, "endurance": 0, "health": 0}
    _items: dict[str, float] = {"strength": 0, "agility": 0, "expertise": 0, "endurance": 0, "health": 0}
    _height: float

    def __init__(self):
        """ Initializes the character and generates its stats and height"""
        self._calculate_stats()
        self._calculate_height()

    def __init__(self, stats: dict[str, float], height: float):
        """ Initializes the character"""
        self._stats = stats
        self._height = height

    def get_atm(self):
        return 0.5 - (3 * self._height - 5) ** 4 + (3 * self._height - 5) ** 2 + self._height / 2

    def get_dem(self):
        return 2 + (3 * self._height - 5) ** 4 - (3 * self._height - 5) ** 2 - self._height / 2

    def get_attack(self):
        return (self._stats["agility"] + self._stats["expertise"]) * self._stats["strength"] * self.get_atm()

    def get_defense(self):
        return (self._stats["endurance"] + self._stats["expertise"]) * self._stats["health"] * self.get_dem()

    def get_performance(self):
        pass

    def get_height(self):
        return self._height

    def _calculate_height(self):
        self._height = random.uniform(1.3, 2.0)

    def _calculate_stats(self):
        """ Calculates the stats for the character """
        self._pick_items()
        self._calculate_strength()
        self._calculate_agility()
        self._calculate_expertise()
        self._calculate_endurance()
        self._calculate_health()

    def _pick_items(self):
        """ Picks the items for the character """
        remaining: int = 150
        item_count: int = 0
        for item in self._items:
            if item_count == self._items.length - 1:
                self._items[item] = remaining
            else:
                value: int = random.randint(0, remaining)
                self._items[item] = value
                remaining -= value

    def _calculate_strength(self):
        self._stats["strength"] = 100 * math.tanh(0.01 * self._items["strength"])

    def _calculate_agility(self):
        self._stats["agility"] = math.tanh(0.01 * self._items["agility"])

    def _calculate_expertise(self):
        self._stats["expertise"] = 0.6 * math.tanh(0.01 * self._items["expertise"])

    def _calculate_endurance(self):
        self._stats["endurance"] = math.tanh(0.01 * self._items["endurance"])

    def _calculate_health(self):
        self._stats["health"] = 100 * math.tanh(0.01 * self._items["health"])


class Warrior(Character):
    _stats: dict[str, float] = {"strength": 0, "agility": 0, "expertise": 0, "endurance": 0, "health": 0}

    def get_performance(self):
        return self.get_attack() * 0.6 + self.get_defense() * 0.4


class Archer(Character):
    _stats: dict[str, float] = {"strength": 0, "agility": 0, "expertise": 0, "endurance": 0, "health": 0}

    def get_performance(self):
        return self.get_attack() * 0.9 + self.get_defense() * 0.1


class Defender(Character):
    _stats: dict[str, float] = {"strength": 0, "agility": 0, "expertise": 0, "endurance": 0, "health": 0}

    def get_performance(self):
        return self.get_attack() * 0.1 + self.get_defense() * 0.9


class Infiltrator(Character):
    _stats: dict[str, float] = {"strength": 0, "agility": 0, "expertise": 0, "endurance": 0, "health": 0}

    def get_performance(self):
        return self.get_attack() * 0.8 + self.get_defense() * 0.3
