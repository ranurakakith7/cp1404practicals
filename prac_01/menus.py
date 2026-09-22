name = input("Enter name: ")
print("Options:\n(H)ello\n(G)oodbye\n(Q)uit")
selection = input("Enter option: ")
while selection != "Q":
    if selection == "H":
        print(f"Hello {name}")
    elif selection == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    selection = input("Enter option: ")
print("Finished.")
