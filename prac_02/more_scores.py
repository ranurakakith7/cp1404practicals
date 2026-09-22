import random


def main():
    number_of_scores = int(input("Number of scores: "))
    with open("results.txt", "w") as file:
        for i in range(number_of_scores):
            score = random.randint(0, 100)
            file.write(f"{score} is {determine_result(score)}\n")
            print(f"{score} is {determine_result(score)}")


def determine_result(score: int):
    """determines result based on the score input"""
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
