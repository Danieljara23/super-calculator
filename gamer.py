import random

nume_ran = random.randint(1, 100)
playing = True

#el jugador
while playing:
    guess = int(input("Ingresa un numero:"))
    if guess == nume_ran:
        playing = False
        print("¡¡Felicidades!! Eres el ganador")
        break
    elif guess > nume_ran:
        print(f"Tu numero: {guess} es mayor")
    elif guess < nume_ran:
        print(f"Tu numero: {guess} es menor")


    #IA del rival
    computador = random.randint(1, 100)
    if computador == nume_ran:
        playing = False
        print(f"Lo siento, pero el numero de tu rival: {computador} es el correcto")
        break
    elif computador > nume_ran:
        print(f"El numero de tu rival: {computador} es mayor")
    elif computador < nume_ran:
        print(f"El numero de tu rival: {computador} es menor")
