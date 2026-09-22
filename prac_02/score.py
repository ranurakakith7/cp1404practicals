"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    print(f"User score {score} is {determine_result(score)}")
    if determine_result(score) == "Excellent":
        print("You get a prize!")
    random_score = random.randint(0, 100)
    print(f"Random: {random_score} = {determine_result(random_score)}")


def determine_result(score):
    if score > 100 or score < 0:
        result = "Invalid"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


main()
