import random
from character_class import Warrior, Archer, Defender, Infiltrator

def gene_mutation(population, p_m, gene):
    for character in population:
        if random.uniform(0,1) < p_m:
            if gene == "height":
                character.set_height(random.uniform(1.3,2))
            elif gene == "items":     
                for item in character.get_items():
                    character.get_items()[item] += random.randint(-1,1)
                character.normalize_items()
            else:
                clases = {
                    1: Warrior,
                    2: Archer,
                    3: Defender,
                    4: Infiltrator,
                }
                character.set_class(clases[random.randint(1,4)])

def limited_multigen(population, p_m, _):
    for character in population:
        if random.uniform(0,1) < p_m:
            M = random.randint(1, 7)
            genes = random.sample(range(1,8), M)

            stats = {
                1: "strength",
                2: "agility",
                3: "expertise",
                4: "endurance",
                5: "health"
            }

            for gene in genes:
                if gene == 6:
                    character.set_height(random.uniform(1.3,2))
                elif gene >= 1 and gene <= 5:
                    character.get_items()[stats[gene]] += random.randint(-1,1)
                    character.normalize_items()
                else:
                    clases = {
                        1: Warrior,
                        2: Archer,
                        3: Defender,
                        4: Infiltrator,
                    }
                    character.set_class(clases[random.randint(1,4)])

def uniform_multigen(population, p_m, _):
    for character in population:
        if random.uniform(0,1) < p_m:
            character.set_height(random.uniform(1.3,2))
        
        if random.uniform(0,1) < p_m:
            clases = {
                1: Warrior,
                2: Archer,
                3: Defender,
                4: Infiltrator,
            }
            character.set_class(clases[random.randint(1,4)])
        
        for item in character.get_items():
            if random.uniform(0,1) < p_m:
                character.get_items()[item] += random.randint(-1,1)
        character.normalize_items()

def complete_mutation(population, p_m):
    for character in population:
        if random.uniform(0,1) < p_m:
            character.set_height(random.uniform(1.3,2))
        
            for item in character.get_items():
                character.get_items()[item] += random.randint(-1,1)
            character.normalize_items()

            clases = {
                1: Warrior,
                2: Archer,
                3: Defender,
                4: Infiltrator,
            }
            character.set_class(clases[random.randint(1,4)])


                    
