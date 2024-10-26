def main():
    cost = 50
    print(f"Amount Due: {cost}")
    while cost > 0:
        cost = validation(cost)
    else:
        print(f"Change Owed: {-cost}")


def validation(cost):
    coin = int(input("Insert Coin: "))
    if coin == 5 or coin == 10 or coin == 25:
        cost = cost - coin
        if cost > 0:
            print(f"Amount Due: {cost}")
        return cost
    elif coin == 50:
        print(f"Amount Due: {cost}")
        return cost
    else:
        print(f"Amount Due: {cost}")
        return cost


if __name__ == '__main__':
    main()
