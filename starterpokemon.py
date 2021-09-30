from random import randint
from termcolor import colored

# version = input("Welche Version spielst du?")

starter = randint(1,3)

if starter == 1:
    wasser = colored('WASSER', 'blue')
    print("Nimm das",wasser,"Pokemon!")
elif starter == 2:
    feuer = colored('FEUER', 'red')
    print("Nimm das", feuer, "Pokemon!")
elif starter == 3:
    pflanze = colored('PFLANZEN', 'green')
    print("Nimm das", pflanze, "Pokemen!")
