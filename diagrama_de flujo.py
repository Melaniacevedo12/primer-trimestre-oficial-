print("___________________________________________________________________________________________")
print("___________________________________________CREDITO_________________________________________")
nombre1 = input("Escriba su nombre: ")
edad=int(input("Escriba su edad: "))
print("--------------------------------------------------------------------------------------------")
if edad >=18:
    print(nombre1,"Puede acceder a su credito")
else:
    (nombre1,"no puede accerder a su credito")
print("---------------------------------------------------------------------------------------------")
print("_______________________________________COSTO DE ENTRADA______________________________________")
nombre2=input("cual es su nombre: ")
edad1=int(input("ingrese su edad: "))
print("-----------------------------------------------------------------------------------------------")
if edad1 <=4 :
    print(nombre2,"entra gratis")
elif edad1 ==5 and edad1 <=18 :
    print(nombre2,"paga 5 euros")
else:
    print(nombre2,"paga 18 euros")
print("-------------------------------------------------------------------------------------------------")

print("_________________________________________________________________________________________________")
print("____________________________________________CALCULADORA__________________________________________")

n1=int(input("ingrese un numero: "))
n2=int(input(" ingrese un numero: "))

print("----------------------------------------------------------------------------------------------------")

operacion=input("Que operacion desea hacer con los numeros: ")

if operacion == "suma":
    print("el resultado de su suama es: ",n1+n2)                                                                    
elif operacion == "resta":
     print("el resultado de su resta es: ", n1-n2)
elif operacion == "multiplicacion" :
    print("el resultado de su multiplicacion es: ", n1*n2)
else:
    print("el resultado de su division es: ", n1//n2)












