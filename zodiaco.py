def signo(dia:int, mes:int):
    if mes == 1:
        if dia>=1 and dia<=20:
            print("Tu signo es capricornio.")
        elif dia>=21 and dia<=31:
            print("Tu signo es acuario.")
        else:
            print("Introduce un dia valido para este mes.")

    elif mes == 2:
        if dia>=1 and dia<=18:
            print("Tu signo es acuario.")
        elif dia>=18 and dia<=28:
            print("Tu signo es piscis.")
        else:
            print("Introduce un dia valido para este mes.")

    elif mes == 3:
        if dia>=1 and dia<=20:
            print("Tu signo es piscis.")
        elif dia>=21 and dia<=31:
            print("Tu signo es aries.")
        else:
            print("Introduce un dia valido para este mes.")

    elif mes == 4:
        if dia>=1 and dia<=19:
            print("Tu signo es aries.")
        elif dia>=20 and dia<=30:
            print("Tu signo es tauro")
        else:
            print("Introduce un dia valido para este mes.")

    elif mes == 5:
        if dia>=1 and dia<=20:
            print("Tu signo es tauro.")
        elif dia>=21 and dia<=31:
            print("Tu signo es geminis")
        else:
            print("Introduce un dia valido para este mes.")

    elif mes == 6:
        if dia>=1 and dia<=20:
            print("Tu signo es geminis.")
        elif dia>=21 and dia<=30:
            print("Tu signo es cancer")
        else:
            print("Introduce un dia valido para este mes.")

    elif mes == 7:
        if dia>=1 and dia<=22:
            print("Tu signo es cancer.")
        elif dia>=23 and dia<=31:
            print("Tu signo es leo")
        else:
            print("Introduce un dia valido para este mes.")

    elif mes == 8:
        if dia>=1 and dia<=22:
            print("Tu signo es leo.")
        elif dia>=23 and dia<=31:
            print("Tu signo es virgo")
        else:
            print("Introduce un dia valido para este mes.")

    elif mes == 9:
        if dia>=1 and dia<=22:
            print("Tu signo es virgo.")
        elif dia>=23 and dia<=30:
            print("Tu signo es libra")
        else:
            print("Introduce un dia valido para este mes.")

    elif mes == 10:
        if dia>=1 and dia<=22:
            print("Tu signo es libra.")
        elif dia>=23 and dia<=31:
            print("Tu signo es escorpio")
        else:
            print("Introduce un dia valido para este mes.")

    elif mes == 11:
        if dia>=1 and dia<=21:
            print("Tu signo es escorpio.")
        elif dia>=22 and dia<=30:
            print("Tu signo es sagitario")
        else:
            print("Introduce un dia valido para este mes.")

    elif mes == 12:
        if dia>=1 and dia<=21:
            print("Tu signo es sagitario.")
        elif dia>=22 and dia<=31:
            print("Tu signo es capricornio")
        else:
            print("Introduce un dia valido para este mes.")

    else:
        print("Introduce un mes valido.")