"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
   - When a function receives an argument with the right data type but invalid value
2. When will a ZeroDivisionError occur?
   - When you attempt to divide a number by zero
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
   - Yes, introduce a while loop which gets the input for the denominator until it isn't zero
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")
