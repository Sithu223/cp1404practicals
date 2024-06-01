def main():
    password = input("Type the password: ")
    MINIMUM_LENGTH = 7
    while len(password) < MINIMUM_LENGTH:
        print("Invalid password")
        password = input("Type the password: ")
    asterisks = len(password) * "*"
    print(asterisks)

main()