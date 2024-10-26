def convert(msg):
    string_msg = str(msg)
    formated_msg = string_msg.replace(":)", "🙂").replace(":(", "🙁")
    return formated_msg


def main():
    message = input("Please enter yours message\n")
    print(convert(message))


if __name__ == '__main__':
    main()
