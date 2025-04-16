import random

while (True):
    p1 = str(input("Player 1: rock(r), paper(p), or scissors(s)?: "))
    randN = random.randrange(3)
    if randN == 0:
        comp = 'r'
        print("computer picked... rock!")
    elif randN == 1:
        comp = 'p'
        print("computer picked... paper!")
    else:
        comp = 's'
        print("computer picked... scissors!")


    if comp == p1:
        print("Draw!")
    elif (p1 == 'r' and comp == 's') or (p1 == 's' and comp == 'p') or (p1 == 'p' and comp == 'r'):
        print("Player wins!")
    else:
        print("Computer wins!")
