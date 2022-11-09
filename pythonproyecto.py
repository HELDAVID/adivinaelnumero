from random import randint

"""
mi primer codigo Helio David Espinosa Contreras
claro algo basico estoy iniciando !!!!

"""
nombre = input('Cual es su nombre: ')
numero_secreto = randint(1,100)
intentos = 0
print(f" Bueno, {nombre} , he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número")


while intentos < 8:
    a = int(input(" Digite un numero: "))
    intentos +=1
    if a < 1:
        print("ha elegido un número que no está permitido. ") 
    elif a > 100:
        print("ha elegido un número que no está permitido. ") 
    elif a < numero_secreto:
        print("respuesta es incorrecta y que ha elegido un número menor al número secreto")
    elif a > numero_secreto: 
        print("respuesta es incorrecta y que ha elegido un número mayor al número secreto")
    elif a == numero_secreto:
        print(f"ha ganado {nombre} y cuántos intentos le ha tomado {intentos}")
        break
else:
    if a != numero_secreto:
        print(f"lo siento se han agotado los intentos, el numero secreto era {numero_secreto}")
        
print(f"el numero era {numero_secreto}")
    



