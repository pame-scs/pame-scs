import random

def Rock_Paper_Scissors():
    u = input("R for Rock, P for Paper and S for Scissors. Chose: ")
    c = random.choice(['R','P','S'])
    print("I choose " + c)
    print("You choose "+ u)
    if c == u:
        print("It's a tie!")
    elif c== 'R' and u == 'S' or c == 'P' and u == 'R' or c == 'S' and u == 'P':
        print("I win!")
    else:
        print("You win!")     
    return 0

def main():
    i = input("Do you want to play Rock, Paper, Scissors? Yes or No: ")
    while i == "Yes":
        Rock_Paper_Scissors()
        i = input("Do you want to play again? Yes or No: ")
    print("Okay! Have a good day!")
    return 0

main()