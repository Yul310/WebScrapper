from random import randint

print("Welcome to Python Casino")
pc_choice = randint(1,50)

user_choice = int(input("Choose number:"))

if user_choice == pc_choice:
    print("You won!")
elif user_choice > pc_choice:
    print("Lower! computer chose",pc_choice)
elif user_choice < pc_choice:
    print("Higher! Computer chose", pc_choice)