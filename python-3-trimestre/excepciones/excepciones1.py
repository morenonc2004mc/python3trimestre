def Nosepuede(): 
    try:
        n = int(input("Ingrse un numero: "))
        t = input("Ingrese un texto: ")
        print("El resultado de la suma es", n+t)
    except TypeError:
            print("No se puede sumar una cadena de texto con un numero")
Nosepuede()