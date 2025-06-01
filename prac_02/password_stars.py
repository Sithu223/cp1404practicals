MINIMUM_LENGTH = 8
def main():
    password = input("Enter your password: ")

    while len(password) < MINIMUM_LENGTH:
        print(f"Password must be at least {MINIMUM_LENGTH} characters.")
        password = input("Enter your password: ")
    print("*" * len(password))

main()
