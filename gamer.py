import random

nume_ran =random.randint(1, 100)
playing = True

while playing:
    guess = int(input("ingresa un numero:"))
    if guess == nume_ran:
        playing = False
        print(f"el numero{guess} es el correcto")
    