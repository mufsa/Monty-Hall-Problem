import random

print("Welcome to the Monty Hall game show! You have a chance to win a car!")
print("Behind one of the three doors, there is a car. Behind the other two, there are goats.")

# Set up the doors and randomly assign the car
doors = ["goat", "goat", "goat"]
car_index = random.randint(0, 2)
doors[car_index] = "car"

# Ask the user to choose a door
choice = int(input("Choose a door (1, 2, or 3): ")) - 1
print("You chose door number", choice + 1)

# Monty opens a goat door
goat_doors = [i for i in range(3) if i != choice and doors[i] == "goat"]
monty_opens = random.choice(goat_doors)
print("Monty opens door number", monty_opens + 1, "to reveal a goat.")

# Ask the user if they want to switch
switch = input("Do you want to switch doors? (yes or no): ")

if switch.lower() == "yes":
    # If the user switches, choose the other unopened door
    new_choice = [i for i in range(3) if i != choice and i != monty_opens][0]
    choice = new_choice

# Determine if the user won the car
if doors[choice] == "car":
    print("Congratulations! You won the car!")
else:
    print("Sorry, you got a goat.")

# Ask the user if they want to see why it's optimal to switch
show_prob = input("Would you like to see why it's optimal to switch? (yes or no): ")
if show_prob.lower() == "yes":
    # Simulate the game 100 times and compare the win percentages for switching vs. not switching
    switch_wins = 0
    stay_wins = 0
    for i in range(100):
        doors = ["goat", "goat", "goat"]
        car_index = random.randint(0, 2)
        doors[car_index] = "car"

        choice = random.randint(0, 2)

        goat_doors = [i for i in range(3) if i != choice and doors[i] == "goat"]
        monty_opens = random.choice(goat_doors)

        if switch.lower() == "yes":
            new_choice = [i for i in range(3) if i != choice and i != monty_opens][0]
            choice = new_choice

        if doors[choice] == "car":
            switch_wins += 1 if switch.lower() == "yes" else 0
            stay_wins += 1 if switch.lower() == "no" else 0
        else:
            stay_wins += 1 if switch.lower() == "yes" else 0
            switch_wins += 1 if switch.lower() == "no" else 0

    print("If you switch, you win", switch_wins, "out of 100 times ({:.2f}%).".format(switch_wins))
    print("If you don't switch, you win", stay_wins, "out of 100 times ({:.2f}%).".format(stay_wins))
else:
    print("Thanks for playing!")