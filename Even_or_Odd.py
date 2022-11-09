
def even_or_odd(x):
    x = x%2
    if x == 0:
        print("Your number is even!")
        return 0
    else:
        print("Your number is odd!")
        return 0

def Main():
    print("Do you want to run the program?")
    i = input("Yes or No: ")
    while i == "Yes":
        x = int(input("Chose a number: "))
        even_or_odd(x)
        i = input("Run it again? Yes or No: ")
    print("Okay have a good day!")
    return 0

Main()