flag = True
n = input("Introduce tu nombre: ")
while (flag== True):#Nombre
    if(n.isalpha()):
        flag = False
    else:
        print("Error de captura. Solo caracteres alfabeticos")
        n = input("Introduce tu nombre: ")
        flag = True
flag = True
edad = (input("Introduce tu edad: "))
while (flag== True):#edad
    if(edad.isdigit()):
        flag = False
    else:
        print("Error de captura. Solo caracteres numericos")
        edad = input("Introduce tu edad: ")
        flag = True
flag = True
print ("Nombre: "+n)
print ("Edad: "+edad)