import random
from rich import print as rprint

#variables
nume_ran = random.randint(1, 100)
playing = True

#El jugador
while playing:
    guess = int(input("Ingresa un numero:"))
    if guess == nume_ran:
        playing = False
        rprint("[deep_pink4]¡¡Felicidades!! [medium_orchid3]Eres el ganador")
        break
    elif guess > nume_ran:
        rprint(f"[green]Tu numero:[red]{guess} [yellow]es mayor") 
    elif guess < nume_ran:
        rprint(f"[green]Tu numero:[red]{guess} [cyan]es menor")

    #IA del rival
    computador = random.randint(1, 100)
    if computador == nume_ran:
        playing = False
        rprint(f"[bright_red]Lo sentimos, pero el numero de tu rival: [green1]{computador} [bright_red]es el correcto")
        break
    elif computador > nume_ran:
        rprint(f"[dark_red]El numero de tu rival:[red]{computador} [yellow]es mayor")
    elif computador < nume_ran:
        rprint(f"[dark_red]El numero de tu rival:[red]{computador} [cyan]es menor")
