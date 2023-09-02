import random
import math


class Character(object):
    def __init__(self, items: dict[str, float] = None, height: float = None):
        """ Initializes the character. If items and height is not provided, generates them"""

        if items is None and height is None:
            self._items = Character._pick_items()
            self._stats = self._calculate_stats()
            self._height = Character._calculate_height()
        else:
            Character._normalize_items(items)
            self._items = items
            self._stats = self._calculate_stats()
            self._height = height

    @staticmethod
    def _normalize_items(self, items: dict[str, float]):
        """ Normalizes the items to sum 150 """
        total:float = 0.0
        for item in items:
            total += items[item]
        
        if total == 150.0:
            return

        factor:float = 150.0 / total
        for item in items:
            items[item] *= factor
        
        
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

    @staticmethod
    def _calculate_height():
        return random.uniform(1.3, 2.0)

    def _calculate_stats(self):
        """ Calculates the stats for the character """
        stats:dict[str, float] = {"strength": 0, "agility": 0, "expertise": 0, "endurance": 0, "health": 0}

        stats["strength"] = self._calculate_strength()
        stats["agility"] = self._calculate_agility()
        stats["expertise"] = self._calculate_expertise()
        stats["endurance"] = self._calculate_endurance()
        stats["health"] = self._calculate_health()

        return stats

    @staticmethod
    def _pick_items():
        """ Picks the items for the character """
        items: dict[str, float] = {"strength": 0, "agility": 0, "expertise": 0, "endurance": 0, "health": 0}
        values = [0] * len(items)

        for i in range (150):
            randomIndex = random.randint(0, 4)
            values[randomIndex] += 1
        
        for item in items:
            items[item] = values.pop()

        return items

    def _calculate_strength(self):
        return 100 * math.tanh(0.01 * self._items["strength"])

    def _calculate_agility(self):
        return math.tanh(0.01 * self._items["agility"])

    def _calculate_expertise(self):
        return 0.6 * math.tanh(0.01 * self._items["expertise"])

    def _calculate_endurance(self):
        return math.tanh(0.01 * self._items["endurance"])

    def _calculate_health(self):
        return 100 * math.tanh(0.01 * self._items["health"])

    def __str__(self):
        return f"Character: \nStats: {self._stats} \nItems: {self._items} \nHeight:{self._height}\n"


class Warrior(Character):

    def get_performance(self):
        return self.get_attack() * 0.6 + self.get_defense() * 0.4


class Archer(Character):

    def get_performance(self):
        return self.get_attack() * 0.9 + self.get_defense() * 0.1


class Defender(Character):

    def get_performance(self):
        return self.get_attack() * 0.1 + self.get_defense() * 0.9


class Infiltrator(Character):

    def get_performance(self):
        return self.get_attack() * 0.8 + self.get_defense() * 0.3
