archivo=input("Ingrese el nombre del archivo con su extensión:  ")

nombre,extension=archivo.split(".")

#print(nombre,extension)

tipo_archivos={"gif":"image/gif",
                "jpg":"image/jpeg",
                "jpeg":"image/jpeg",
                "png":"image/png",
                "pdf":"application/pdf",
                "txt":"text/plain",
                "zip":"application/zip"}
print("\n")


for t in tipo_archivos:
    if extension == t:
        print("Salida esperada: {}".format(tipo_archivos[t]))
    
    elif extension not in tipo_archivos:
        print("application/octet-stream")
        break 