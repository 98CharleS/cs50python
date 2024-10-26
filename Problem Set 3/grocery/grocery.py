list = {}


def main():
    try:
        x = input().upper()
        if x not in list:
            list[x] = 1
            main()
        elif x in list:
            y = list[x]
            list[x] = y + 1
            main()
        else:
            main()
    except EOFError:
        for item in sorted(list):
            print(f"{list[item]} {item}")


if __name__ == '__main__':
    main()
