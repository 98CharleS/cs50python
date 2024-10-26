import re


def main():
    print(count(input("Text: ")))


def count(s):
    try:
        pattern = "(^|\W)um($|\W)"
        value = re.findall(pattern, s, re.IGNORECASE)
        n = len(value)
        if value:
            return n
    except (ValueError, KeyboardInterrupt):
        return EOFError

if __name__ == "__main__":
    main()
