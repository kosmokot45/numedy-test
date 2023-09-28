import secrets
import string
from collections import defaultdict
import numpy as np

brands = ["Tefal", "Zagovor", "LG", "Dell", "Nokia", "Yandex"]

models = [
    f"model_{secrets.randbelow(10)}_{secrets.choice(string.ascii_lowercase)}"
    for model in range(100)]


def get_balance():
    items = np.random.default_rng().normal(loc=2.5, scale=1, size=100)
    numbers_dict = defaultdict(int)
    for item in items:
        number = int(item)
        if number < 0:
            number = 0
        elif number > 4:
            number = 4
        numbers_dict[number] += 1

    return [numbers_dict[i] for i in range(5)]
