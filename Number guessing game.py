#========Number guessing game=======
#========Import libraries=======
import random

#========Functions=======
# Function to randomly select a number between 1 and 100
def draw_num():
    random_num = random.randint(1, 100)
    return random_num


#========Game sectioon=======
easy_count = 10
hard_count = 5
aim_num = draw_num()
print(aim_num)


while True:
    diff_level = input('''Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard': ''')
    
    if diff_level == 'easy':
        while True:
            if easy_count > 0:
                print(f"You have {easy_count} attempts remaining to guess the number.")
                easy_count -= 1
                p_guess = int(input("Make a guess: "))
                if p_guess > aim_num:
                    print("Too high.\nGuess again.")
                elif p_guess < aim_num:
                    print("Too low.\nGuess again.")
                elif p_guess == aim_num:
                    print(f"You got it! The answer is {aim_num}")
                    exit()
            else:
                print("You've run out of guesses, you lose")
                exit()

    elif diff_level == 'hard':
        while True:
            if hard_count > 0:
                print(f"You have {hard_count} attempts remaining to guess the number.")
                hard_count -= 1
                p_guess = int(input("Make a guess: "))
                if p_guess > aim_num:
                    print("Too high.\nGuess again.")
                elif p_guess < aim_num:
                    print("Too low.\nGuess again.")
                elif p_guess == aim_num:
                    print(f"You got it! The answer is {aim_num}")
                    exit()
            else:
                print("You've run out of guesses, you lose")
                exit()
    
    else:
        print("Invalid input. Please try again\n")

