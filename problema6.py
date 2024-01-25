edad_cliente=int(input("Digite su edad actual en años: "))

if edad_cliente <4:
    print("Entrada Gratis.")
elif edad_cliente>=4 and edad_cliente<=18:
    print("Costo de entrada -> 5$")
else:
    print("Costo de entrada -> 10$") 
    