#Adivina el numero
import random
bandera = True
i = 1
num = random.randrange(1,50)
print (num)
while (bandera == True):
    n = int(input("En que numero estoy pensando?"))
    if (n == num):
        print("Felicidades! Acertaste con tu "+ str(i) +" intento" )
        bandera = False 
    else:
        print("Error, intentalo denuevo")
        i=i+1
