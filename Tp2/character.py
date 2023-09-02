import random

class Character(object):
    """ Represents a character in the game """

    _stats:dict[str, float] = {"strength": 0, "agility": 0, "expertise": 0, "endurance": 0, "health": 0}


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

