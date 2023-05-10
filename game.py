import random

def generate_random_number(low,high):
    return random.randint(low, high)

def play_game():
    low = 1
    high = 100
    target_number = generate_random_number(low, high)
    attempts = 0

    print ("welkome to the game")
    print ("i have number what is it?")

    while True :
        guess = int(input("ur choise"))
        attempts += 1

        if guess < target_number:
            print("its wrong")
        elif guess > target_number:
            print("its wrong")
        else:
            print("congratulations in {attempts}.")
            break


    play_again = input("once more?" (y/n):)
    if play_again.lower() == "y":
    play_game()
else:
print("ty bye")

play_game()