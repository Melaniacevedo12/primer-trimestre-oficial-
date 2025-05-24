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