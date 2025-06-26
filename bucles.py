# print("_________________________________________________________________________________________")
# print("-------------------------------------------EJERCICIO 1----------------------------------------")

# total=0

# num1=int(input("Ingrese un numero ( 0 para terminar): "))

# while num1 != 0 :
#     total += num1
#     print(f"El total es: {total}")

# print("-------------------------------------------EJERCICIO 2---------------------------------------")


# contraseña=int(input("ingrese la contraseña: ")).lower()

# while contraseña != "python123" :
#     print("contraseña incorrecta")
#     contraseña=int(input("intenta de nuevo:")).lower()
# print("acceso concendido")

# print("-------------------------------------------EJERCICIO 3---------------------------------------")

# producto=[]  
# producto.append(input("ingrese el primere producto: "))
# producto.append(input("ingrese el segundo producto: "))

# while True:
#     productoo=input("escribe algo(o escribe 'final'para saber sus productos): ").lower()
#     if productoo == "final":
#         break
# print(f"tus productos son: {producto}")

#print("-------------------------------------------EJERCICIO 4---------------------------------------")
#
#contador=0
#pares=0
#impares=0
#
#while contador < 9:
#    num=int(input(f"ingrese el numero {contador + 1}: "))
#    if num %2 == 0:
#        pares += 1
#    else:
#        impares +=1
#    contador += 1
#print("catidad de pares:",pares)
#print("catidad de impares:",impares)
#
#print("-------------------------------------------EJERCICIO 5---------------------------------------")
#
#print("ingrese notas de 0 a 5 con numeros enteros NO deccimales")

notas=[]  
notas.append(int(input("ingrese la primera nota: ")))
notas.append(int(input("ingrese la segunda nota: ")))
notas.append(int(input("ingrese la tercera nota: ")))
notas.append(int(input("ingrese la cuarta nota: ")))
notas.append(int(input("ingrese la quinta nota: ")))


while True:
    p=input("escribe algo(o escribe 'salir'para saber sus notas): ").lower()
    if p == "salir":
        break
print(f"tus notas son: {notas}")

promedio= notas // 5 

print(f"tu promedio es: {promedio}")


















