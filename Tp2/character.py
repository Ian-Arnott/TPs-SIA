import random

class Character(object):

    _stats: dict[str, float] = {"strength": 0, "agility": 0, "expertise": 0, "endurance": 0, "health": 0}
    _height = random.uniform(1.3, 2.0)

    def get_atm(self):
        return 0.5 - (3 * self._height - 5) ** 4 + (3 * self._height - 5) ** 2 + self._height / 2

    def get_dem(self):
        return 2 + (3 * self._height - 5) ** 4 - (3 * self._height - 5) ** 2 - self._height / 2
    def pick_stats(self):
        """ Picks the stats for the character """
        remaining:int = 150
        statCount:int = 0
        for stat in self._stats:
            if statCount == self._stats.length - 1:
                self._stats[stat] = remaining
            else:
                value:int = random.randint(0, remaining)
                self._stats[stat] = value;
                remaining -= value

    def get_attack(self):
        return (self._stats["agility"] + self._stats["expertise"]) * self._stats["strength"] * self._height

    def get_defense(self):
        return (self._stats["endurance"] + self._stats["expertise"]) * self._stats["health"] * self._height

    def get_performance(self):
        pass


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
