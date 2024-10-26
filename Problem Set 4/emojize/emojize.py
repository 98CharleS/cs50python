import emoji

x = input("Input: ")

y = [":thumbsup:"]

if x in y:
    x = "👍"
if x == "hello, :earth_asia:":
    x = "hello, 🌏"


print(emoji.emojize(x))
