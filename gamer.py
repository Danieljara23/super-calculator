import random

nume_ran = random.randint(1, 100)
playing = True

computador = random(1, 100)

while playing:
    guess = int(input("ingresa un numero:"))
    if guess == nume_ran:
        playing = False
        print(f"el numero{guess} es el correcto")
    elif guess > nume_ran:
        print(f"el numero {guess} es mayor")
    elif guess < nume_ran:
        print(f"el numero {guess} es menor")
    
    if 