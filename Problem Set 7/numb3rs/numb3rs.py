import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        digits = ip.split(".")
        if all(0 <= int(digit) <= 255 for digit in digits):
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    main()
