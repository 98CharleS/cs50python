from PIL import Image, ImageOps
import sys
import os

valid_extensions = [".jpg", ".jpeg", ".png"]

first = os.path.splitext(sys.argv[1])[1].lower()
second = os.path.splitext(sys.argv[2])[1].lower()


def checking_input():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    try:
        Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")


def checking_extensions(f, s):
    if f not in valid_extensions or s not in valid_extensions:
        sys.exit("Invalid input")
    if f != s:
        sys.exit("Input and output have different extensions")


def making_img():
    img = Image.open(sys.argv[1])
    shirt = Image.open("shirt.png")
    size = shirt.size
    img = ImageOps.fit(img, size)
    img.paste(shirt, shirt)
    img.save(sys.argv[2])


def main():
    checking_input()
    checking_extensions(first, second)
    making_img()


main()
