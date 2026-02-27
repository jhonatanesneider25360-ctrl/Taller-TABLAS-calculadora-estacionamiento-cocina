from clase_parqueadero import Parqueadero


# ========= Programa principal =========
parqueadero = Parqueadero()

while True:
    print("\n--- MENU ---")
    print("1. Agregar registro")
    print("2. Mostrar registros")
    print("3. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        parqueadero.agregar_registro()

    elif opcion == "2":
        parqueadero.mostrar_registros()

    elif opcion == "3":
        print("Programa finalizado")
        break

    else:
        print("Opcion invalida")