import random


def main():
    x = input("Level: ")
    try:
        x = int(x)
    except ValueError:
        main()
    if x < 1:
        main()
    else:
        y = random.randint(1, x)
        guessing(x, y)


def guessing(a, b):
    c = input("Guess: ")
    try:
        c = int(c)
    except ValueError:
        guessing(a, b)
    if c > a:
        print("Too large!")
        guessing(a, b)
    if c > b:
        print("Too large!")
        guessing(a, b)
    elif c < b:
        print("Too small!")
        guessing(a, b)
    elif c == b:
        print("Just right!")


if __name__ == '__main__':
    main()
