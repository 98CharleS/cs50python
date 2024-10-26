def range(c):
    if c <= 1:
        print("E")
    elif c >= 99:
        print("F")
    else:
        print(f"{int(c)}%")


def main():
    try:
        x, y = input("Fraction: ").split("/")
        try:
            x = int(x)
            y = int(y)
            if x > y:
                main()
            else:
                c = (x / y) * 100
                range(round(c))
        except(ValueError, ZeroDivisionError):
            main()
    except ValueError:
        main()


if __name__ == '__main__':
    main()
