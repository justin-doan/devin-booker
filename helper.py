import random

def get_random_quote(filename):
    with open(filename, "r", encoding='utf-8') as f:
        quotes = [line.strip() for line in f]
    return random.choice(quotes)