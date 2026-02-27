from usuario import Usuario
from calculadora import Calculadora

def principal():
    """
    Punto de entrada del programa. 
    Aquí creamos los objetos principales y manejamos el menú.
    """
    print("--- CALCULADORA MODULAR POO ---")
    nombre = input("Dime tu nombre: ")
    cedula = input("Dime tu cedula: ")
    
    # Instanciamos (creamos) el objeto usuario
    user = Usuario()
    user.set_nombre(nombre)
    user.set_cedula(cedula)
    
    # Instanciamos la calculadora
    calc = Calculadora()

    while True:
        print(f"\nHola {user.nombre}, elige una opción:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Ver Historial")
        print("6. Salir")
        
        opc = input("\nOpcion: ")

        if opc == "6":
            print("Cerrando sistema...")
            break
            
        if opc == "5":
            calc.imprimir_tabla()
            continue

        op_nombres = {"1": "suma", "2": "resta", "3": "multiplicacion", "4": "division"}
        
        if opc in op_nombres:
            try:
                n1 = float(input("Número 1: "))
                n2 = float(input("Número 2: "))
                
                res = calc.calcular(user, n1, n2, op_nombres[opc])
                if res is not None:
                    print(f"\n>>> RESULTADO: {res}")
            except ValueError:
                print("\n[!] Error: Ingresa solo números.")
        else:
            print("\n[!] Opción no válida.")

if __name__ == "__main__":
    principal()
