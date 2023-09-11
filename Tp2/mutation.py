import random

def gene_mutation(population, p_m, gene):
    for character in population:
        if random.uniform(0,1) < p_m:
            if gene == "height":
                character.set_height(random.uniform(1.3,2))
            elif gene == "items":     
                for item in character.get_items():
                    while True:
                        change = random.uniform(-1,1)
                        if character.get_items()[item] + change > 0:
                            character.get_items()[item] += change
                            break
                character.normalize_items()


def limited_multigen(population, p_m, _):
    for character in population:
        if random.uniform(0,1) < p_m:
            M = random.randint(1, 6)
            genes = random.sample(range(1,7), M)

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
                    while True:
                        change = random.uniform(-1,1)
                        if character.get_items()[stats[gene]] + change > 0:
                            character.get_items()[stats[gene]] += change
                            break
                    character.normalize_items()


def uniform_multigen(population, p_m, _):
    for character in population:
        if random.uniform(0,1) < p_m:
            character.set_height(random.uniform(1.3,2))
        
        for item in character.get_items():
            if random.uniform(0,1) < p_m:
                while True:
                    change = random.uniform(-1,1)
                    if character.get_items()[item] + change > 0:
                        character.get_items()[item] += change
                        break
        character.normalize_items()


def complete_mutation(population, p_m, _):
    for character in population:
        if random.uniform(0,1) < p_m:
            character.set_height(random.uniform(1.3,2))
        
            for item in character.get_items():
                while True:
                    change = random.uniform(-1,1)
                    if character.get_items()[item] + change > 0:
                        character.get_items()[item] += change
                        break
            character.normalize_items()


                    
