x, y, z = input("Expression: ").strip().lower().split(sep=" ")


def calc(d, b, e):
    a = int(d)
    c = int(e)
    if b == "+":
        return a + c
    elif b == "-":
        return a - c
    elif b == "*":
        return a * c
    elif b == "/":
        return a / c


print("%.1f" % calc(x, y, z))
