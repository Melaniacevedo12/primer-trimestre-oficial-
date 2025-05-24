print("SISTEMAS DE CALIFICACIÓN")
print("Esto es un programa que requerira de sus datos personales, para poder ingresar su usario y saber sus notas finales del las materias")
print("en base de la información anterior requiremos sus datos personales:")
estudiante=input("Por favor ingresar su nombre: ")
print("""El estudiante sera calificado de la siguiente manera
            -  NIVEL DE CALIFICACIÓN -
            -  NOTA  -  ASIGNATURA   -
            -   5    - SUPERIOR      -  
            -   4    - ALTO          -
            -   3    - BASICO        -
            -   2    - BAJO          -
            -   1    - INSUFICIENTE  -
Donde la nota minima para pasar es 3 la nota que este por debajo de esta, se considerara perdida""")
print("SOCIALES")

nota1=int(input("ingrese su primera nota:"))
nota2=int(input("ingrese su segundo nota:"))
nota3=int(input("ingrese su tercera nota:"))
op1=(nota1+nota2+nota3)//3
print(estudiante,"su nota final de sociales fue de: ",op1)
print("-------------------------------------------------------------------------------------------------------")
print("MATEMATICAS")
not1=int(input("ingrese su primera nota:"))
not2=int(input("ingrese su segundo nota:"))
not3=int(input("ingrese su tercera nota:"))
op2=(not1+not2+not3)/3
print(estudiante,"su nota final de matematicas fue de: ",op2)
print("-------------------------------------------------------------------------------------------------------")
print("HUMANIDADES")
no1=int(input("ingrese su primera nota:"))
no2=int(input("ingrese su segundo nota:"))
no3=int(input("ingrese su tercera nota:"))
op3=(no1+no2+no3)/3
print(estudiante,"su nota final de humanidades fue de: ",op3)
print("-------------------------------------------------------------------------------------------------------")
print("ETICA")
n1=int(input("ingrese su primera nota:"))
n2=int(input("ingrese su segundo nota:"))
n3=int(input("ingrese su tercera nota:"))
op4=(n1+n2+n3)/3
print(estudiante,"su nota final de etica fue de: ",op4)
print("-------------------------------------------------------------------------------------------------------")
print("EMPRENDIMIENTO")
a1=int(input("ingrese su primera nota:"))
a2=int(input("ingrese su segundo nota:"))
a3=int(input("ingrese su tercera nota:"))
op5=(a1+a2+a3)/3
print(estudiante,"su nota final de emprendimiento fue de: ",op5)
print("-------------------------------------------------------------------------------------------------------")
print("PROMEDIO DEL ESTUDIANTE")
promedio=op1+op2+op3+op4+op5
print("el estudiante",estudiante,"tuvo ub promedio de: ",promedio)