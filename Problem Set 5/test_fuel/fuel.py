def gauge(c):
    if c <= 1:
        return "E"
    elif c >= 99:
        return "F"
    else:
        return f"{int(c)}%"


def main():
    try:
        f = input("Fraction: ")
        f_c = convert(f)
        print(f_c)
    except ValueError:
        main()


def convert(fraction):
    x, y = fraction.split("/")
    if not x.isdigit() or not Y.isdigit():
        raise ValueError
    if int(y) == 0:
        raise ZeroDivisionError
    if int(x) > int(y):
        raise ValueError
    c = (x / y) * 100
    return gauge(round(c))


if __name__ == '__main__':
    main()
