password = input("Password: ")
min_length = 8
while len(password) < min_length:
    print("Invalid, needs to be at least 8 characters")
    password = input("Password: ")
print("*" * len(password))
