import random

with open("temps_input.txt", "w") as file:
    for i in range(15):
        file.write(f"{random.uniform(-200, 200)}\n")
