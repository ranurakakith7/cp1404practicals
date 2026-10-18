# 1
out_file = open("data.txt", "w")
out_file.write(input("Name: "))
out_file.close()

# 2
in_file = open("data.txt", "r")
name = in_file.read().strip()
print(f"Hi {name}!")
out_file.close()

# 3
with open("numbers.txt") as in_file:
    num1 = int(in_file.readline())
    num2 = int(in_file.readline())
print(f"Total: {num1 + num2}")

