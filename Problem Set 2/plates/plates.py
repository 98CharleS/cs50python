import re


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 1 < len(s) < 7:
        if re.search("^[A-Z]{2}.*", s):
            if re.search("^[A-Z]{2,6}$", s) or re.search("^[A-Z]{2,6}([1-9][0-9]*)$", s):
                return True


main()
