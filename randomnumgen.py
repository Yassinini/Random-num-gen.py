import random
print("Welcome to my number guessing game.\n")
print("I am thinking of a number between 1 and 100.\n")
print("You have 5 attempts to guess the number.\n")
number = random.randint(1,100)

print("please select difficulty level")
easy=5
medium=10
hard=15
print("easy")
print("medium")
print("hard")
choice=input()
if choice=="easy":
    print("you have 15 attempts to guess the number.")
    Tries=15
elif choice=="medium":
    print("you have 10 attempts to guess the number.")
    Tries=10
elif choice=="hard":
    print("you have 5 attempts to guess the number.")
    Tries=5
else:
    print("invalid choice")

for attempt in range(Tries):
    guess=int(input("enter a number between 1 and 100:  "))
    if guess<number:
        print("too low")
    elif guess>number:
        print("too high")
    elif guess==number:
        print("correct")
    else:
        print("Didn't get it. Better luck next time!")
        break
        exit()