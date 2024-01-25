time=input("Digite la hora actual: ")
print(time)
horas=int(time.split(":")[0])
minutos=int(time.split(":")[1])

if horas >= 7 and horas <= 8:
    if minutos >=0 and minutos <=59:
        print("Es hora del desayuno")
    
elif horas >= 12 and horas <= 13:
    if minutos >=0 and minutos <=59:
        print("Es hora del almuerzo")

elif horas >=18 and horas <=19:
    if minutos >= 0 and minutos <=59:
        print("Es hora de la cena") 
