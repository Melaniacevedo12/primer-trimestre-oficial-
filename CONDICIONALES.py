# 
# print("---------------------------------------------------------------------------------")

# n1=int(input("ingresa un numero"))
# n2=int(input("ingresa un numero"))

# op=n1*n2
# print(op)


# if op<=30:
#     print(" el resultado es menor que treinta")
# elif op<=10000:
#     print("el resultado es mayor de diez mil")
# else:
#     print("su numero se paso de lo requerido")
# print("-----------------------------------------------------------------------------------------")
# print("----------------------------------------------------------------------------------")
print("************************************** GENERACION DIGITAL ***************************************")
#debe de ser menor que este
usuario=int(input("coloque su fecha de nacimiento: "))

if usuario <= 1940 :
    print("usted pertenece a la generacion silenciosa")
elif usuario <=1964 :
    print("usted pertenece  a la generacion baby boomer")
elif usuario <=1979 :
    print("usted pertenece  a la generacion x")
elif usuario <=2000 :
    print("usted pertenece  a la generacion y")
elif usuario <=2010 :
    print("usted pertenece  a la generacion z")
else:
    print("su edad no esta clasificada en ninguna generacion")