import random

def Guess(n):
    x = random.randint(0,n)
    print("You have 3 guess!")
    i = 0
    while i < 3:
        i += 1
        if i != 3:
            g=int(input("Your guess is? "))
            if g == x:
                print("You win!")
            elif g < x:
                print("Try upper")
            elif g > x:
                print("Try lower")
        elif i==3 and g!=x:
            g=int(input("this is your last guess "))
            if g == x:
                print("You win!")
            elif g < x:
                print("You lose")
            elif g > x:
                print("You lose")
    print(x)

def Main():
    print("Do you want to play \"Guess the number\" ")
    x = input("Yes or No: ")
    while x == "Yes":
        print("okay")
        n = int(input("What's the highest number you want to guess?> "))
        Guess(n)
        x = input("You want to play again? Yes or No: ")
    if x == "No":
        print("Okay! Have a good day!")

Main()
