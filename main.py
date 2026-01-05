import random

number = random.randint(1, 50)
guess = int(input("1–50 orasida son kiriting: "))

if guess == number:
    print("Topdingiz! Son:", number)
else:
    print("Xato! Son:", number)
