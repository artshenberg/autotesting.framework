import random
import string


def random_text(lenth=5):
    # get letters
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(lenth))


def random_digit(minimal=0, maximal=5, step=1):
    # get digit
    return random.randrange(minimal, maximal, step)
