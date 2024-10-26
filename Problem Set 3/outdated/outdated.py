import re

month = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

month_dic = {mon: idx for idx, mon in enumerate(month, start=1)}

separators = r"[ /]"


def main():
    try:
        x = input("Date : ")
        if re.search("^[0-9]{2} [A-Z]*.*", x):
            main()
        if re.search("^[A-Z][a-z]*/.*", x):
            main()
        if re.search("^[A-Z][a-z]* [0-9]+ [0-9]+", x):
            main()

        m, d, y = re.split(separators, x.replace(",", "").strip())

        if m.isdigit():
            m = int(m)
        else:
            if m not in month_dic:
                print("Invalid month name.")
                return main()
            m = month_dic[m]

        d = int(d)
        y = int(y)

        if m > 12 or d > 31:
            print("Invalid date.")
            return main()

        print(f"{y}-{m:02}-{d:02}")
    except (EOFError, ValueError):
        print("Error: Please enter a valid date.")


if __name__ == '__main__':
    main()
