print("_________________________________________________________________________________________")
print("-------------------------------------------EJERCICIO 1----------------------------------------")

resul=0
while True:
    num1=int(input("Ingrese un numero ( 0 para terminar): "))
    if num1 == 0 :
        break
    resul += num1
    print(f"el total de la suma es de : {resul}")


    
print("-------------------------------------------EJERCICIO 2---------------------------------------")

pasword=""

while pasword != "python123" :
    pasword=input("ingrese la contraseña: ")
print("contraseña correcta")
  
print("-------------------------------------------EJERCICIO 3---------------------------------------")

compras=[]  

producto=input("Agregar otro producto (o escribir 'fin para finalizar') ")

while producto.lower() != "fin" :
    compras.append(producto)
    producto=input("Agregar otro producto (o escribir 'fin para finalizar') ")

print(f"tu lista de compras: {compras}")

print("-------------------------------------------EJERCICIO 4---------------------------------------")

contador=0
pares=0
impares=0
while contador < 9:
    num=int(input(f"ingrese el numero {contador + 1}: "))
    if num %2 == 0:
        pares += 1
    else:
        impares +=1
    contador += 1
print("catidad de pares:",pares)
print("catidad de impares:",impares)

print("-------------------------------------------EJERCICIO 5---------------------------------------")

print("ingrese notas de 0 a 5 con numeros enteros NO decimales")

notas = []

while True:
    entrada = input("Ingresa una nota (o 'salir' para terminar): ")
    if entrada == "salir":
        break
    nota = float(entrada)
    if 0 <= nota <= 5:
        notas.append(nota)
promedio = sum(notas) // len(notas) if notas else 0
print(f"Promedio de calificaciones:{promedio}  , su lista es:{notas}" )

print("-------------------------------------------EJERCICIO 6---------------------------------------")

numer=int(input("Ingresa un número para ver su tabla: "))
tabla = 1
while tabla <= 10:
    print(f"{numer} x {tabla} = {numer * tabla}")
    tabla += 1

print("-------------------------------------------EJERCICIO 7---------------------------------------")

secreto = 17
intento = -1
while intento != secreto:
    intento = int(input("Adivina el número secreto: "))
    if intento < secreto:
        print("Demasiado bajo.")
    elif intento > secreto:
        print("Demasiado alto.")
print("¡Correcto!")

print("-------------------------------------------EJERCICIO 8---------------------------------------")

frutas = ("manzana", "pera", "banana", "uva")
while True:
    intento = input("Adivina una fruta: ")
    if intento in frutas:
        print("¡Correcto!")
        break
    else:
        print("No está, intenta otra vez.")

print("-------------------------------------------EJERCICIO 9---------------------------------------")

dic = {"hola": "hello", "adiós": "goodbye", "gracias": "thanks", "por favor": "please", "gato": "cat"}
while True:
    palabra = input("Palabra en español (o 'salir'): ")
    if palabra == "salir":
        break
    if palabra in dic:
        print("Traducción:", dic[palabra])
    else:
        print("No está en el diccionario.")


print("-------------------------------------------EJERCICIO 10---------------------------------------")

while True:
    print("\nMenú:\n1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Salir")
    opcion = input("Elige una opción: ")
    if opcion == "5":
        break
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))
    if opcion == "1":
        print(f"Resultado: {a + b} ")
    elif opcion == "2":
        print(f"Resultado: {a - b}")
    elif opcion == "3":
        print(f"Resultado: {a * b}")
    elif opcion == "4":
        if b != 0:
            print(f"Resultado: {a // b}")
        else:
            print("No se puede dividir por cero.")


print("-------------------------------------------EJERCICIO 11---------------------------------------")

personas = {}
nombre = input("Nombre (o 'salir'): ")
while nombre.lower() != "salir":
    edad = int(input("Edad: "))
    personas[nombre] = edad 
    nombre = input("Nombre (o 'salir'): ")
    
print(f"Registro de personas:{personas}")

print("-------------------------------------------EJERCICIO 12---------------------------------------")

colores = ["rojo", "azul", "verde", "amarillo", "negro"]
while True:
    intento = input("Escribe un color: ")
    if intento in colores:
        print("¡Color encontrado!")
        break
    else:
        print("No está, intenta de nuevo.")

print("-------------------------------------------EJERCICIO 13---------------------------------------")

num = int(input("Ingresa un número: "))
i = 1
while i <= 5:
    print(f"{num}^{i} = {num ** i}")
    i += 1

print("-------------------------------------------EJERCICIO 14---------------------------------------")

cuadrados = []
o = 0
while o < 5:
    n = int(input("Número: "))
    cuadrados.append(n ** 2)
    o += 1
print("Lista de cuadrados:", cuadrados)

print("-------------------------------------------EJERCICIO 15---------------------------------------")

estudiantes = {}
while True:
    nombre = input("Nombre del estudiante (o 'fin'): ")
    if nombre == "fin":
        break
    nota = float(input("Nota final: "))
    estudiantes[nombre] = nota
print("Estudiantes registrados:", estudiantes)
