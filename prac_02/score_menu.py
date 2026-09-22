def main():
    score = 0
    print("Menu:\n(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit")
    option = input("Option: ").upper()
    while option != "Q":
        if option == "G":
            score = get_valid_score()
        elif option == "P":
            print(f"Result: {determine_result(score)}")
        elif option == "S":
            show_stars(score)
        else:
            print("Invalid option")
            print("Menu:\n(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit")
        option = input("Option: ").upper()
    print("Farewell")


def get_valid_score() -> int:
    score = int(input("Score: "))
    while score > 100 or score < 0:
        print("Invalid!")
        score = int(input("Score: "))
    return score


def determine_result(score: int) -> str:
    if score > 100 or score < 0:
        result = "Invalid"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


def show_stars(score):
    print("*" * score)


main()
