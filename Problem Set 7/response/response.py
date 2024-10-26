import validators

mail = input("What's your email address? ")


def validation(m):
    if validators.email(m) == True:
        return "Valid"
    else:
        return "Invalid"


print(validation(mail))
