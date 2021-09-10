#Palindromo -> palabra que leida alrevez significa lomismo
palabra = []
#Captura de palabras
for i  in range (0,5):
    print("Introduce una palabra")
    palabra.append(input())
#Revision de palindromo
for i in palabra:
    palabrareversa = i[::-1]
    if (palabrareversa == i):
        print(i , " Es un palindromo")
    else:
        print(i ," No es un palindromo")

