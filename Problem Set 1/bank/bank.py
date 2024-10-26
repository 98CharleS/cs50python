x = input("Greeting: ").strip().lower()


def main(mes):
    print(value(mes))


def value(greeting):
    if "hello" in greeting:
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")


if __name__ == '__main__':
    main(x)
