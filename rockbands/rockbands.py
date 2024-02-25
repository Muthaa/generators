import os
import random

def generate_username(num_results=1):
    dir_path = os.path.dirname(__file__)
    adjectives, nouns = [], []
    with open(os.path.join(dir_path, 'data', 'adjectives.txt'), 'r') as file_a:
        with open(os.path.join(dir_path, 'data', 'wordbank.txt'), 'r') as file_n:
            for line in file_a:
                adjectives.append(line.strip())
            for line in file_n:
                nouns.append(line.strip())

    usernames = []
    for _ in range(num_results):
        adjective = random.choice(adjectives)
        noun = random.choice(nouns).capitalize()
        random_num = str(random.randrange(10))
        usernames.append(adjective + noun + random_num)
    
    return usernames