text = input("Introduce tu texto")
arreglo = text.split()
Acronimo=""
for palabra in arreglo:
    Acronimo = Acronimo + palabra[0] + " "
print (Acronimo)