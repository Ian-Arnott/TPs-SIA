import random
import math
from character_class import Class, Warrior, Infiltrator, Defender, Archer


class Character(object):
    def __init__(self, character_class:Class = None, items: dict[str, float] = None, height: float = None):
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
        if character_class is None:
            self._class = Character._pick_class()
        else:
            self._class = character_class

    @staticmethod
    def from_genotype(genotype: list[float]):
        """ Creates a character from a genotype """
        items = {"strength": genotype[0], "agility": genotype[1], "expertise": genotype[2], "endurance": genotype[3], "health": genotype[4]}
        height = genotype[5]
        char_class = genotype[6]

        return Character(char_class, items, height)

    @staticmethod
    def _normalize_items(items: dict[str, float]):
        """ Normalizes the items to sum 150 """
        total:float = 0.0
        for item in items:
            total += items[item]
        
        if total == 150.0:
            return

        factor:float = 150.0 / total
        for item in items:
            items[item] *= factor

    def normalize_items(self):
        Character._normalize_items(self._items)
        self._stats = self._calculate_stats()
        
    def get_atm(self):
        return 0.5 - (3 * self._height - 5) ** 4 + (3 * self._height - 5) ** 2 + self._height / 2

    def get_dem(self):
        return 2 + (3 * self._height - 5) ** 4 - (3 * self._height - 5) ** 2 - self._height / 2

    def get_attack(self):
        return (self._stats["agility"] + self._stats["expertise"]) * self._stats["strength"] * self.get_atm()

    def get_defense(self):
        return (self._stats["endurance"] + self._stats["expertise"]) * self._stats["health"] * self.get_dem()

    def get_performance(self):
        return self._class.attack_mod * self.get_attack() + self._class.defense_mod * self.get_defense()

    def get_height(self):
        return self._height
    
    def set_height(self, height):
        self._height = height
    
    def get_items(self):
        return self._items
    
    def set_class(self, character_class):
        self._class = character_class

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
    def _pick_class():
        """ Picks the class for the character """
        classes = {
            0: Warrior,
            1: Archer,
            2: Defender,
            3: Infiltrator
        }
        index = random.randint(0,3)
        return classes[index]

    @staticmethod
    def _pick_items():
        """ Picks the items for the character """
        items: dict[str, float] = {"strength": 0, "agility": 0, "expertise": 0, "endurance": 0, "health": 0}
        values = [0] * len(items)

        for _ in range (150):
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
    
    def get_genotype(self) -> list[float]:
        genes = []
        for item in self._items:
            genes.append(self._items[item])
        genes.append(self._height)
        genes.append(self._class)
        return genes 

    def __str__(self):
        return f"Character: \nClass: {self._class} \nStats: {self._stats} \nItems: {self._items} \nHeight:{self._height}\n" 
