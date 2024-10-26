def main():
    txt = input("Input: ")
    print(f"Output: {shorten(txt)}")

def shorten(word):
    output = word.replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "").replace("A", "").replace("E", "").replace("I", "").replace("O", "").replace("U", "")
    return output

if __name__ == "__main__":
    main()
