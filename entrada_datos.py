from enum import auto


nombre_completo = input("Ingresa tu nombre y apellido: ") # str

edad = int(input("Ingresa tu edad: "))

altura = float(input("Ingresa tu altura: "))

autorizacion = input("¿Autorizas el programa? (si/no): ") == "si"

print(autorizacion)

print("Gracias, excelente dia.")