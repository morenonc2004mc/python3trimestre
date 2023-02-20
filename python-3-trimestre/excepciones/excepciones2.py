diccionario = {"Vaca": "cow", "Caballo": "Horse", "Perro": "Dog", "Delfin": "Dolphin"}
def clave():
    try:
        clave=input("Ingrese un animal: ")
        diccionario[clave]
    except KeyError:
        print("La clave no existe")    
clave()


    
