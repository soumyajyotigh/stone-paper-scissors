import random

# Rock Paper Scissors
def gameWin(comp, you):
    # If two values are equal, it's a tie!
    if comp == you:
        return None

    # when computer chose rock
    elif comp == 'r':
        if you=='s':
            return 0
        elif you=='p':
            return 1
    
    # when computer chose paper
    elif comp == 'p':
        if you=='r':
            return 0
        elif you=='s':
            return 1
    
    # when computer chose scissors
    elif comp == 's':
        if you=='p':
            return 0
        elif you=='r':
            return 1

print("Computer's Turn: rock(r) paper(p) or scissors(s)?")
randomNo = random.randint(1, 3) 
if randomNo == 1:
    comp = 'r'
elif randomNo == 2:
    comp = 'p'
elif randomNo == 3:
    comp = 's'

you = input("Your Turn: rock(r) paper(p) or scissors(s)?")
g = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if g == None:
    print("The result is a tie!")
elif g:
    print("You Win!")
else:
    print("You Lose!")