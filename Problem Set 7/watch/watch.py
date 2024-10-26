import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    prefix = "https://youtu.be/"
    link = re.search(r"<iframe src=\"(?:https?://)?(?:www.)?youtube\.com/embed/(xvFZjo5PgG0)\"", s)
    try:
        yt_link = prefix+link.group(1)
        return yt_link
    except AttributeError:
        return None


if __name__ == "__main__":
    main()
