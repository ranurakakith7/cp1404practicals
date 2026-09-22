def main():
    min_length = 8
    password = get_password(min_length)
    print_asterisks(password)


def print_asterisks(password: str):
    print("*" * len(password))


def get_password(min_length: int) -> str:
    password = input("Password: ")
    while len(password) < min_length:
        print("Invalid, needs to be at least 8 characters")
        password = input("Password: ")
    return password


main()
