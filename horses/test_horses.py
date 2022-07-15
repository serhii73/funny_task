import random
import string

from horses import get_top3


def generate_name():
    return "".join(
        [
            random.choice(string.ascii_letters),
            random.choice(string.ascii_letters),
            random.choice(string.ascii_letters),
            random.choice(string.ascii_letters),
            random.choice(string.ascii_letters),
        ]
    )


horses1 = {
    "Daniel": 100,
    "John": 2,
    "Mary": 3,
    "Bob": 4,
    "Jane": 5,
    "Jack": 6,
    "Jill": 7,
    "Joe": 8,
    "Juan": 9,
    "Jill2": 10,
    "Leon": 110,
    "Navar": 12,
    "Colby": 13,
    "Midnightflame": 14,
    "Marengo": 15,
    "Explorer": 16,
    "Madison": 17,
    "Morning Ranger": 18,
    "Salsa2": 19,
    "Blanca": 20,
    "Bellator": 21,
    "Salsa": 22,
    "Doulton": 23,
    "Cheyenne": 24,
    "Rusty": 25,
}


horses2 = {generate_name(): v for v in range(25)}

horses3 = {generate_name(): random.randint(1, 1000) for _ in range(25)}


def test_horse1():
    top_3_horses = get_top3(horses1)
    assert top_3_horses == ["Leon", "Daniel", "Rusty"]


def test_horse2():
    top_3_horses = get_top3(horses2)
    top_3_horses_value = [horses2.get(i) for i in top_3_horses]
    assert top_3_horses_value == [24, 23, 22]


def test_horse3():
    top_3_horses = get_top3(horses3)
    sorted_i = dict(sorted(horses3.items(), key=lambda item: item[1]))
    assert list(sorted_i)[-3:][::-1] == top_3_horses
