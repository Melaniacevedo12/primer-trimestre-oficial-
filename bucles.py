 print("_________________________________________________________________________________________")
 print("-------------------------------------------EJERCICIO 1----------------------------------------")
 total=0
 num1=int(input("Ingrese un numero ( 0 para terminar): "))
 while num1 != 0 :
     total += num1
     print(f"El total es: {total}")
 print("-------------------------------------------EJERCICIO 2---------------------------------------")
 contraseña=int(input("ingrese la contraseña: ")).lower()
 while contraseña != "python123" :
     print("contraseña incorrecta")
     contraseña=int(input("intenta de nuevo:")).lower()
 print("acceso concendido")
 print("-------------------------------------------EJERCICIO 3---------------------------------------")
 producto=[]  
 producto.append(input("ingrese el primere producto: "))
 producto.append(input("ingrese el segundo producto: "))
 while True:
     productoo=input("escribe algo(o escribe 'final'para saber sus productos): ").lower()
     if productoo == "final":
         break
 print(f"tus productos son: {producto}")
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

print("ingrese notas de 0 a 5 con numeros enteros NO deccimales")

notas = []
while True:
    entrada = input("Ingresa una nota (o 'salir' para terminar): ")
    if entrada == "salir":
        break
    nota = float(entrada)
    if 0 <= nota <= 5:
        notas.append(nota)
promedio = sum(notas) / len(notas) if notas else 0
print("Promedio de calificaciones:", promedio)

print("-------------------------------------------EJERCICIO 6---------------------------------------")

numero12=int(input("Ingresa un número para ver su tabla: "))
tabla = 1
while tabla <= 10:
    print(f"{numer012} x {tabla} = {numero12 * tabla}")
    tabla += 1




















