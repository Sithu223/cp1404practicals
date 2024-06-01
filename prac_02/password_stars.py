def main():
    get_password()


def get_password():
    password = input("Type the password: ")
    MINIMUM_LENGTH = 7
    while len(password) < MINIMUM_LENGTH:
        print("Invalid password")
        password = input("Type the password: ")
    have_password(password)


def have_password(password):
    asterisks = len(password) * "*"
    print(asterisks)


main()