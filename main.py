playing = True

while playing:
    num1 = int(input("Ingresa el número 1:"))
    num2 = int(input("Ingresa el número 2:"))

    print("Ingresa la operacion que deseas hacer:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    user_input = int(input())

    if user_input == 1:
        print("La suma es...", num1 + num2)
    elif user_input == 2:
        print("La resta es...", num1 - num2)
    elif user_input == 3:
        print("La Multiplicacion es...", num1 * num2)
    elif user_input == 4:
        print("La Division es...", num1 / num2)
        
playing = False