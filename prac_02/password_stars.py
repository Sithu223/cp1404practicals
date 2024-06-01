def main():
    get_password()


def get_password():
    password = input("Type the password: ")
    MINIMUM_LENGTH = 7
    while len(password) < MINIMUM_LENGTH:
        print("Invalid password")
        password = input("Type the password: ")
    print_asterisks(password)


def print_asterisks(password):
    asterisks = len(password) * "*"
    print(asterisks)


main()