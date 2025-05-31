print("------------------------------------------------------------------------")

print("********************************* TALLER 1 ********************************")

nombre=input("Cual es el nombre del producto: ")
precio=float(input("Cual es el precio del producto: "))
cantidad=int(input("Cual es la cantidad del producto: "))
tupli=(nombre,precio)
lis=[tupli,cantidad]
dic={
    "producto":nombre
}
total=precio*cantidad
print("---------------------------------------------------------------------------------")
print("Resumen de la compra")
print("producto: " , nombre)
print("precio unitario: " , precio)
print("cantidad: ", cantidad)
print("costo total: ",total)
("--------------------------------------------------------------------------------------------")

print("********************************* TALLER 2 ********************************")

no1=input("Cual es el nombre del primer producto: ")
no2=input("Cual es el nombre del segundo producto: ")
no3=input("Cual es el nombre del tercer producto: ")
#acontinuación siguiente linea el precio unitario
preci1=float(input("Cual es el precio del primer producto: "))
preci2=float(input("Cual es el  precio del segundo producto:"))
preci3=float(input(" Cual es el precio del tercer producto : "))
#acontinuación siguiente linea la cantidad del producto
cantida1=int(input("Cual es la cantidad del primer producto que ingreso producto:  "))
cantida2=int(input("Cual es la cantidad del segundo producto que ingreso producto: "))
cantida3=int(input("Cual es la cantidad del tercer producto que ingreso producto: "))
#crearemos la tupla que se nos requirio
tupli1=(no1,preci1)
tupli2=(no2,preci2)
tupli3=(no3,preci3)
#crearemos la lista que se nos solocita
lis1=[tupli1,cantida1]
lis2=[tupli2,cantida2]
lis3=[tupli3,cantida3]
#creamos un diccionario
dic1={
    "1producto":no1,
    "2producto":no2,
    "3producto":no3
    }
#precio*cantidad
total1=preci1*cantida1
total2=preci2*cantida2
total3=preci3*cantida3
print("----------------------------------------------------------------------------")
print("Resumen de la compra")
print("producto: " , nombre)
print("producto: " , nombre)
print("producto: " , nombre)
print("producto: " , nombre)
print("precio unitario: " , precio)
print("cantidad: ", cantidad)
print("costo total: ",total)
print("---------------------------------------------------------------------------------")

print("**************************************** TALLER 3 ****************************************")
print("-------------------------------------------------------------------------------------------")

print("***************************************** REGISTRO DE NOTAS DE UN ESTUDIATE *****************************************")

print("En este sistema se le pedira su nombre de usuario, nombre de las asignaturas, notas y al final se le dara su boletin")
print("NOMBRE DE USIARIO")

nombre=input("Ingrese su nombre")

print("NOMBRE DE LAS ASIGNATURAS")

asignatura1=input("ingrse el nombre de la asignatura")
asignatura2=input("ingrse el nombre de la asignatura")
asignatura3=input("ingrse el nombre de la asignatura")

print("NOTA DE CADA ASIGNATURA")
print(asignatura1)
nota1=float(input("ingress la primera nota de la asignatura de",asignatura1,": "))
nota2=float(input("ingress la segunda nota de la asignatura de",asignatura1,": "))
promedio1=(nota1+nota2)/2


print(asignatura2)
nota3=float(input("ingress la primera nota de la asignatura de",asignatura2,": "))
nota4=float(input("ingress la segunda nota de la asignatura de",asignatura2,": "))
promedio2=(nota3+nota4)/2


print(asignatura3)
nota5=float(input("ingress la primera nota de la asignatura de",asignatura3,": "))
nota6=float(input("ingress la segunda nota de la asignatura de",asignatura3,": "))
promedio3=(nota5+nota6)/2

print("--------------------------------------------------------------------")

tupla1=(asignatura1,promedio1)
tupla2=(asignatura2,promedio2)
tupla3=(asignatura3,promedio3)

print("-----------------------------------------------------------------")

lita=[asignatura1,nota1,nota2]
lita=[asignatura2,nota3,nota4]
lita=[asignatura3,nota5,nota6]

print("---------------------------------------------------------------------")

diccionario={ "nombre": nombre,
    "materias":asignatura1,
    "materias":asignatura2,
    "materias":asignatura3
}

promedio=(promedio1+promedio2+promedio3)/3

print("-----------------------------------------------------------------------")
print("*********************************BOLETIN*******************************")
print("nombre del estudiante es:",nombre)
print(asignatura1,promedio1)
print(asignatura2,promedio2)
print(asignatura3,promedio3)
print("el promedio del estudiante es:",promedio)
print("***********************************************************************")













