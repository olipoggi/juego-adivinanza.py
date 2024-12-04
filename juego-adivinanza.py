import random

numero_secreto = random.randint (1,100)
cantidad_intentos = 0
cantidad_max_intentos = 5
adivinado = False

print ("¡Bienvenido al juego de adivinar el número secreto!")

while not adivinado:
    if not cantidad_intentos < cantidad_max_intentos:
         print ("Game over! sos un desastre, que tengas un buen día :)")
         break
    entrada = input("Introduce un número del 1 al 99: ")
    numero = int(entrada)

    if numero == numero_secreto:
        print("¡Felicitaciones adivinaste whojoo!")
        adivinado = True
    elif numero < numero_secreto:
        print("El número secreto es mayor al que ingresaste")
    else: 
        print("El numero secreto es menor al que ingresaste")
    cantidad_intentos += 1 



