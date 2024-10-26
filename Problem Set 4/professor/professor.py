import random


def main():
    score = 0
    level = get_level()
    for i in range(10):
        d1 = generate_integer(level)
        d2 = generate_integer(level)
        score = score + calc(d1, d2)
    print(f"Score: {score}")


def get_level():
    x = input("Level: ")
    try:
        x = int(x)
    except ValueError:
        get_level()
    if x < 1:
        get_level()
    if x > 3:
        get_level()
    return x


def generate_integer(level):
    if level == 1:
        d1 = 0
    else:
        d1 = 10 ** (level - 1)
    d2 = 10**level
    n = random.randint(d1, d2)
    return n


def calc(d1, d2):
    error = 0
    r = d1 + d2
    ur = input(f"{d1} + {d2} = ")
    while error < 2:
        try:
            ur = int(ur)
        except ValueError:
            print("EEE")
            error = error + 1
            ur = input(f"{d1} + {d2} = ")
        if r == ur:
            return 1
        else:
            print("EEE")
            error = error + 1
            ur = input(f"{d1} + {d2} = ")
    print("EEE")
    print(f"{d1} + {d2} = {r}")
    return 0


if __name__ == "__main__":
        main()
