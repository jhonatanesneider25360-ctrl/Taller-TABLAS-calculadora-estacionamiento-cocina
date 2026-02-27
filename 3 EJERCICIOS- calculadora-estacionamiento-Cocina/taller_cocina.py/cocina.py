# =========================
# CLASE PRINCIPAL: COCINA
# =========================

from clases import Ingrediente, Cuchillo, Olla


class Cocina:

    def __init__(self):
        self.inventario = ["Olla", "Cebolla", "Tomate", "Pastas", "Agua"]
        self.requeridos = ["Olla", "Cebolla", "Tomate", "Pastas", "Agua"]
        self.cuchillo = Cuchillo()
        self.cebolla = Ingrediente("Cebolla")
        self.tomate = Ingrediente("Tomate")
        self.olla = Olla()

    def verificar_ingredientes(self):
        if all(item in self.inventario for item in self.requeridos):
            print(" Ingredientes verificados. Menú desbloqueado.\n")
            return True
        else:
            print(" Faltan ingredientes.")
            return False

    def combate(self):
        while not (self.cebolla.procesado and self.tomate.procesado):

            print("\n1. Cortar Cebolla")
            print("2. Cortar Tomate")
            print("3. Afilar cuchillo")

            opcion = input("Elige una opción: ")

            if opcion == "1":
                self.cuchillo.cortar(self.cebolla)
            elif opcion == "2":
                self.cuchillo.cortar(self.tomate)
            elif opcion == "3":
                self.cuchillo.afilar()

    def cocinar(self):
        self.olla.agregar(self.cebolla)
        self.olla.agregar(self.tomate)

        print("\n Comienza la cocción...")
        self.olla.hervir()

    def iniciar(self):
        if self.verificar_ingredientes():
            self.combate()
            self.cocinar()
