menu = {
    "baja taco": 4.25,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}

dishes = []

price = 0

for f in menu:
    dishes.append(f)


def main(y):
    try:
        x = input("Item: ").lower()
        if x in dishes:
            y = y + menu[x]
            print(f"Total: $" "%.2f" % y)
            main(y)
        else:
            main(y)
    except EOFError:
        None


if __name__ == '__main__':
    main(price)
