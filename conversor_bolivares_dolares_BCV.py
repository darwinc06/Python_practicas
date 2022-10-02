mensaje = 'BIENVENIDOS AL CONVERSOR DE MONEDAS DOLARES A BOLIVARES (2022)'
print(mensaje)

precio_dolar = float(input("Ingresa la tasa de cambio BCV: "))
dolares = float(input("Ingresa la cantidad de dólares: "))
bolivares = dolares * precio_dolar
print(f"Los {dolares} dólares equivalen a {bolivares} bolivares")
