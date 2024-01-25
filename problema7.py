numero1=int(input("Ingrese el primer número:  "))
numero2=int(input("Ingrese el segundo número: "))

print("\n----------MENU DEL PROGRAMA----------\n")
print("""   1. Mostrar una suma de los dos números
            2. Mostrar una resta de los dos números
            3. Mostrar una multiplicación de los dos números
            4. Salir del programa\n""")
opcion=int(input("Ingrese una opción:  "))

if opcion == 1:
    print("Suma de números: {}".format(numero1+numero2))
elif opcion == 2:
    print("Resta de números: {}".format(numero1-numero2))
elif opcion == 3:
    print("Producto de números: {}".format(numero1*numero2))
elif opcion == 4:
    print("!Hasta Luego!")
    exit
else:
    print("Opción inválida para el programa")
 
 