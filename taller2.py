print("___________________________________________________________________________________________")
print("--------------------taller de condiccionales y diagrams de flujo---------------------------")
print("___________________________________________________________________________________________")
print("--------------------Ejercicio de condiciones y operaciones matematicas---------------------")

print("*****************************************ejercicio 1****************************************")

print("Este programa esta enfocado en mostrale al usuario si su numero es mayo , menor o igual que cero")

numero=int(input("Ingrese un numero: "))

if numero == 0:
    print("el numero es igual a 0") 
elif numero < 0 :
    print("su numero es menor que cero")
else:
    print("su numero es mayo que cero")

print("*****************************************ejercicio 2****************************************")

print("Este requerira que ud ingrese dos numeros en el cual se le indiacar cual es mayor de los numeros registrados")

numero10=int(input("Ingrese un numero: "))
numero2=int(input("Ingrese un numero: "))

if numero10 < numero2 or numero2 > numero10:
    print(numero10,"es mayo que",numero2,) 
    print (numero2 , "es mayo que numero",numero10 ) 
else:
    print("no se acepta decimales en el sistema,espere la proxima actializacion")

print("*****************************************ejercicio 3****************************************")

print("Este programa le dira si el numero que cocoque es par")

number=int(input("Ingrese un numero: "))

if number 2 % == 0:                         #profe la verdad nose cual es error
    print("el numero es par")
else:
    ("el numero es impar")

print("*****************************************ejercicio 4 ****************************************")

print("indoca si el umero esta entre 10 y 20")

nu=int(input("Ingresa un numero: "))

if nu>10 and nu<20 :
    print(" el numero se encuentra entre 10 y 20")
else:
    print("su numero no se encuentra entre 10 y 20")

print("*****************************************ejercicio 5 ****************************************")

print("dado tres numeros , encuentra el mayor de su condicional")

no1=int(input("Ingresa un numero: "))
no2=int(input("Ingresa un numero: "))
no3=int(input("Ingresa un numero: "))

if no1 > no2 and no1 > no3:
    print(no1,"es el numero mayor de los 3 numero que ud ingreso")
elif no2 > no1 and no2 > no3:
    print(no2,"es el numero mayor de los 3 numero que ud ingreso")
else:
    (no3,"es el numero mayor de los 3 numero que ud ingreso")

print("*****************************************ejercicio 6****************************************")

print("calcula el precio final con un 10% de descuento si el total es mayor a 100 ")

precio=int(iput("ingrese su precio final: "))

if precio > 100:
    descuento=10*precio/100
    print("se realiza un descuento del 10%,el precio final actual de su producto es:",precio-descuento)
else:
    print("su precio final aplica para el 10%,su precio final es de: ",precio)

print("*****************************************ejercicio 7 ****************************************")

print("verificar si la persona puede votar tinene que ser mayor de edad")

eda=int(iput("ingrese su edad: "))

if eda >= 18:
    print("usted puede votar")
else:
    print("no tine la edad requerida para votar")

print("*****************************************ejercicio 8 ****************************************")

print("tipo de cliente determinar si es normal o vip")

valor=int(input("ingrse su precio: "))
SI=int(iput("usted es cilete VIP (SI) O (NO): ")).upper

if SI == "SI":
    re=valor*20%/100
    print("se realiza un descuento del 20% por ser cliente VIP",re)
else:
    print("usted es cliente normal no se le realizara el 20% de descuento ")

print("*****************************************ejercicio 9 ****************************************")

print("el numero tiene que ser multiplo de 3 y de 5")

num=int(iput("ingrese un numero: "))

if num%3==0 and nu%5==0:
    print("el numeor es multiplo de 3 y 5")
elif num%3==0:
    print("el numero es multiplo de 3")
elif nu%5==0:
     print("el numero es multiplo de 5")
else:
    print("no es multiplo ni 3 de ni de 5")

print("*****************************************ejercicio 10 ****************************************")

print("Determine si el numero es divisible entre otros")

nem1=int(input("ingrse un numero para saber si en divivsible: "))
nem2=int(input("ingrse el primer numero para saber es divisor: "))
nem3=int(input("ingrse el segundo numero para saber es divisor: "))

if nem1%nem2=0 and nem1//nem2==0:
    print("el numero es divisor por los dos numeros que usted ingreso")
elif nem1%nem2=0:
    print("el numero es divisible solo por: ",nem2)
elif nem1%nem3=0:
    print("el numero es divisible solo por: ",nem2)
else:
    print("el numer no es divisible por ningunp de los dos numers ingresados")

print("___________________________________________________________________________________________")
print("--------------------Ejercicio de condiciones y listas---------------------")
print("___________________________________________________________________________________________")
print("*****************************************ejercicio 11 ****************************************")

print("crear una lista de 5 numeros y realizar lo demas que dice enste ejercicio ")

list=[]

list.apped=int(input("input ingrese un numero: "))
list.apped=int(input("input ingrese un numero: "))
list.apped=int(input("input ingrese un numero: "))
list.apped=int(input("input ingrese un numero: "))
list.apped=int(input("input ingrese un numero: "))
print(list)
if list[2] < 10:
    print("el numero es menor a 10") 
elif list == 10: 
    print("su igual a 10")
else:
    print("el numero es mayor a 10")

print("*****************************************ejercicio 12 ****************************************")

print("vereficar si el numero 7 esta en la lista")

lista1=[3,5,"",9]
num34.apped=int(input("ingrese un numero ",[2]))

if 7 in lista1 == 7:
    print("el numero 7 si se encuentra en la lista") 
else:
    print("el numero 7 no se encuatra en la lista:")

print("*****************************************ejercicio 13 ****************************************")

print("sume los dos primeros numeros de la lista")

list4=[4,6,2,8]

if lista4[0]+lista4[1] > 10:
    print("suma alta") 
else: 
    print("su suma es baja")

print("*****************************************ejercicio 14 ****************************************")

print("mostrar el untimo nombre de la lista")

lista23=["ana","luis","pedro","marta"]

if lista23[-1]:
    print("nombre correcto") 
else: 
    print("nombre diferente")

print("*****************************************ejercicio 15 ****************************************")

print("cambio de color")

lista0=["blaco","amarillo","negro"]

if lista0[1] == "azul":
    lista0[1]="rojo"
    print("la lista ha sido actualizada",lista0)
else:
    print("el color no es azual. por lo cual la sita sigue igual")

print("___________________________________________________________________________________________")
print("-----------------------------Ejercicio de condiciones y tuplas--------------------------------------")

print("*****************************************ejercicio 16****************************************")

print("ordene la tupla")

tupla=(5,8,12,20)

if tupla[0] > tupla[-1]:
    pirnt("orden ascendente")
else:
    ("orden descendente")

print("*****************************************ejercicio 17****************************************")

print("si el segundo valor es mayor a 30")

tupla=(25,32,28)

if tupla1[1] > 30:
    print("edad mayor a 30")
else:
    print("edad menor o igual a 30")

print("*****************************************ejercicio 18****************************************")

print("cambio de tupla a lista,etc")

tuplaqq=(1,2,3)
lista=list(tuplaqq)

if  lista [1] == 2:
    lista [1]= 10

tupla=tuple(tuplaqq)
print(tupla)

print("*****************************************ejercicio 19****************************************")

print("dada una tupla aceder a su sengundo valor")

tupl=(4,5)

if tupl [1] > 5:
    print("coordenada alta")
else:
    print("coordenada baja")

print("*****************************************ejercicio 20****************************************")

print("dada las tuplas deben se ser iguales si no se cumple lo dicho el programa termina")

tuplita1=(3,4)
tuplita2=(3,5)

if tuplita1 == tuplita2:
    print("tuplas iguales")
else:
    print("tupla diferente")

print("___________________________________________________________________________________________")
print("--------------------Ejercicio de condiciones y operaciones matematicas---------------------")
print("___________________________________________________________________________________________")

print("*****************************************ejercicio 21****************************************")

print("crea un deccionario con lo requerido en el ejercico")

nom1=input("cual es su nombre: ")
edad1=int(input("ingrese su edad: "))

diccionario={ 
             "nombre":nom1,
             "edad":edad1
}

if edad1 >= 18:
    print("mayor de edad")
else:
    print("menor de edad")

print("*****************************************ejercicio 22****************************************")

print("crear un diccionario si es mayor a 18 cambiarlo por 21")

nom2=input("cual es su nombre: ")
edad2=int(input("ingrese su edad: "))

diccionario1={ 
             "nombre":nom2,
             "edad":edad2
}

if diccionario1["edad2"] >18:
    diccionario1["edad"]=21
    print("diccionario1")

else:
    print("fin")

print("*****************************************ejercicio 23****************************************")

nom8=input("cual es su nombre: ")

usuario={"nombre":nom8}

if "ciudad" not in usuario:         # el " not in " sirve para verificar si un valor NO está contenido dentro de una secuencia, como una lista, tupla o cadena
    usuario["ciudad"]="Bogota"  
    print(usuario)   
else:
    print("fin") 

print("*****************************************ejercicio 24****************************************")

print("verificar si la clave existe")

product={  
    "producto": "pan" ,
    "precio":1200
}

if "precio" in product:
    print(product["precio"])
else:
    print("no hay precio")

print("*****************************************ejercicio 25****************************************")

prod={    
    "pan":1200,
    "leche":2000
}

if "pan" in prod:
    print(prod["pan"])
else:
    print("producto no disponible")
