#Piedra papel o tijera
bandera = True
print("USUARIO 1")
print("1-Pierdra 2-Papel 3-Tijera")
j1 = input("Introduce el numero de tu jugada: ")
while (bandera == True):
    if (j1== "1" or j1 == "2" or j1=="3"):
        bandera = False
    else:
        print("Se introdujo un valor erroneo")
        j1 = input("Introduce el numero de tu jugada: ")
        bandera = False
bandera=True
print("USUARIO 2")
print("1-Pierdra 2-Papel 3-Tijera")
j2 = input("Introduce el numero de tu jugada: ")
while (bandera == True):
    if (j2== "1" or j2 == "2" or j2=="3"):
        bandera = False
    else:
        print("Se introdujo un valor erroneo")
        j2 = input("Introduce el numero de tu jugada: ")
        bandera = False
#Comparacion de jugadas
if((j1 == "1" and j2 == "1" )or(j1=="2" and j2=="2") or (j1=="3" and j2=="3")):
    print("Empate")
elif((j1=="1" and j2=="3")or (j1=="2" and j2=="1") or (j1=="3" and j2=="2")):
    print("Gana J1")
else:
    print("Gana J2")