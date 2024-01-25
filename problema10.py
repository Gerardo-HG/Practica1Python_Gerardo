lista_de_muestra=["Rojo","Verde","Blanco","Negro","Rosa","Amarillo"]
lista_modificada=[]
#for i,e in enumerate(lista_de_muestra):
    #print(i,e)

for i,e in enumerate(lista_de_muestra):
    if i == 1 or i==2 or i==3:
        lista_modificada.append(lista_de_muestra[i])

print("\n")

for l in lista_modificada:
    print(l) 
