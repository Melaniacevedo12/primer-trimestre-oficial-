print("----------------------------------------------------------------------------")
print("ejercicio 1")
jo="el conocimiento es poder"
es=jo.find("conocimiento")
print(es)
sa=jo.find("poder")
print(sa)
print("-----------------------------------------------------------------------------")
print("ejercicio 2")
k="la practica hace al maestro"
ex=k.find("practica")
print(ex)
et=k.find("maestro")
print(et)
print("-----------------------------------------------------------------------------------")
print("ejecicio 3")
ingrese=input("ingrese una frase:")
palabra=input("ingrese la palabra que quiere buscar")#corregir
e=ingrese.find("palabra")
print(e)
print("-------------------------------------------------------------------------------------")
print("ejercicio 4")
texto1="Doña Uzeada de Ribera Maldonado de Bracamonte y Anaya era baja, rechoncha, abigotada. Ya no existia razon para llamar talle al suyo. Sus colores vivos, sanos, podian mas que el albayalde y el soliman del afeite, con que se blanqueaba por simular melancolias. Gastaba dos parches oscuros, adheridos a las sienes y que fingian medicamentos. Tenia los ojitos ratoniles, maliciosos. Sabia dilatarlos duramente o desmayarlos con recato o levantarlos con disimulo. Caminaba contoneando las imposibles caderas y era dificil, al verla, no asociar su estampa achaparrada con la de ciertos palmizpedos domesticos. Sortijas celestes y azules le ahorcaban las falanges"
encontrar=texto1.find("Sabia")
print(encontrar)
encontra=texto1.find("Caminaba")
print(encontra)
encon=texto1.find("falanges")
print(encon)
extraer=texto1[459:657]
print(extraer)
texto2="El oeste de Texas divide la frontera entre Mexico y Nuevo México. Es muy bella pero aspera, llena de cactus, en esta region se encuentran las Davis Mountains. Todo el terreno esta lleno de piedra caliza, torcidos arboles de mezquite y espinosos nopales. Para admirar la verdadera belleza desertica, visite el Parque Nacional de Big Bend, cerca de Brownsville. Es el lugar favorito para los excurcionistas, acampadores y entusiastas de las rocas. Pequeños pueblos y ranchos se encuentran a lo largo de las planicies y cañones de esta region. El area solo tiene dos estaciones, tibia y realmente caliente. La mejor epoca para visitarla es de Diciembre a Marzo cuando los dias son tibios, las noches son frescas y florecen las plantas del desierto con la humedad en el aire."
print(texto2.find("oeste"))
print(texto2.find("nopales"))
extroaer=texto2[3:253]
print(extroaer)
print("------------------------------------------------------------------------------------------------------------")
print("ejercicio 5")
nombre=input("ingrese su nombre")
nota1=float(input("porfavor ingrese su nota:"))
nota2=float(input("porfavor ingrese su nota:"))
nota3=float(input("porfavor ingrese su nota:"))
oper1=nota1*0.20
print(oper1)
oper2=nota2*0.3
print(oper2)
oper3=nota3*0.5
print(oper3)
resultado=oper1+oper2+oper3
resultad=resultado//3
print("su nota final fue de",resultad)

