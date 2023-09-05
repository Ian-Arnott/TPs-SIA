import random
import math

def uniform_multigen(population, p_m):
    for character in population:
        if random.uniform(0,1) < p_m:
            character.set_height(random.uniform(1.3,2))
        
        for item in character.get_items():
            #print(character.get_items()[item])
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

def limited_multigen(population, p_m):
    for character in population:
        if random.uniform(0,1) < 1:
            M = random.randint(1, 6)
            genes = random.sample(range(1,7), M)
            #print(genes)

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
                else:
                    character.get_items()[stats[gene]] += random.randint(-1,1)
            character.normalize_items()


                    
