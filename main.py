from zodiaco import signo

def cuadrado(a):
    return a*4

def triangulo(b, h):
    return (b*h)/2

def circulo(radio:float):
    return 3.1416*radio**2

def numeroe(limite:int):
    e = f = 1.0
    for i in range(2, limite):
        e += 1.0/f
        f *=i
    return e

while True :
    print("1). Calcular area de cuadrado, triangulo y circulo.")
    print("2). Signo zodiacal.")
    print("3). Numero e.")
    print("0). Salir.")
    opc = input("Que desea hacer: ")

    if opc == "1":
        while True:
            print("1). Cuadrado.")
            print("2). Triangulo.")
            print("3). Circulo.")
            print("x). Salir.")
            op = input("Que area desea calcular: ")

            if op == "1":
                lado = float(input("Introduzca la medida de uno de los lados: "))
                print("El area de la figura es: ", cuadrado(lado))
                
            if op == "2":
                base = float(input("Introduzca la base del triangulo: "))
                altura = float(input("Introduzca la altura del triangulo: "))
                print("El area es: ", triangulo(base, altura))
                
            if op == "3":
                radio = float(input("Introduzca el radio del circulo: "))
                print("El area es: ", circulo(radio))
                
            if op == "x":
                break

    elif opc == "2":
        dia = int(input("Introduce tu dia de nacimiento: "))
        mes = int(input("Introduce tu mes de nacimiento"))
        signo(dia, mes)
    elif opc == "3":
        limite = int(input("Introduce el limite (Mayor limite, mas precision del numero)"))
        print(numeroe(limite))
    elif opc == "0":
        print("Saliendo...")
        break
    else:
        print("")
        print("Opcion no valida. Introduzca otra.")








