import re

i = ["gif", "jpeg", "png"]
a = ["pdf", "zip", "txt"]

file_name = input("File name: ").strip().lower()


def checking_dots(n):
    if re.search(r".*\..*\..*", n):
        x, y, c = file_name.split(sep=".")
        main(c)
    elif re.search(r".*\..*", n):
        x, y = file_name.split(sep=".")
        main(y)
    else:
        print("application/octet-stream")


def main(n):
    if n in i:
        print(f"image/{n}")
    elif n == "jpg":
        print(f"image/jpeg")
    elif n == "txt":
        print(f"text/plain")
    elif n in a:
        print(f"application/{n}")
    else:
        print("application/octet-stream")


if __name__ == '__main__':
    checking_dots(file_name)
