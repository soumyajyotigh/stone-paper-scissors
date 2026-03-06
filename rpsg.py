import random


ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'
emojis = { ROCK: '✊', SCISSORS: '✂️', PAPER: '📄' }
choices = tuple(emojis.keys())
def gameWin(comp, you):
    # If two values are equal, it's a tie!
    if comp == you:
        return None

    # when computer chose rock
    elif comp == 'r':
        if you=='p':
            return 1
        elif you=='s':
            return 0
    
    # when computer chose paper
    elif comp == 'p':
        if you=='s':
            return 1
        elif you=='r':
            return 0
    
    # when computer chose scissors
    elif comp == 's':
        if you=='r':
            return 1
        elif you=='p':
            return 0


user_score = 0
comp_score = 0


while True:
    randomNo = random.randint(1, 3) 
    if randomNo == 1:
        comp = 'r'
    elif randomNo == 2:
        comp = 'p'
    elif randomNo == 3:
        comp = 's'

    you = input("Your Turn: rock(r) paper(p) or scissors(s)?\n")
    g = gameWin(comp, you)

    print(f"Computer chose {emojis[comp]}")
    print(f"You chose {emojis[you]}")

    if g == None:
        print("The result is a tie!")
    elif g:
        print("You Win!")
        user_score += 1
    else:
        print("You Lose!")
        comp_score += 1


    print(f"Score: You {user_score} - Computer {comp_score}")
    play = input("Play again? (yes/y or no/n): ").lower()

    if play in ('yes','y'):
        continue
    elif play in ('no','n'):
        break
    else:
        print("Invalid input")    
    