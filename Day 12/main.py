import art
import random


print(art.logo)

rand = random.randint(0, 100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
e_h = input("Choose a difficulty. Type 'easy' or 'hard':")
print(rand)
a = 0
if e_h == "easy":
    a = 10
else : a = 5

while a != 0:
    print(f"You have {a} attempts remaining to guess the number.")
    choice = int(input("Make a guess: "))
    if choice > rand:
        print("high")
    elif choice < rand:
        print("low")
    elif choice == rand:
        print("you win")
        break
    a -= 1
