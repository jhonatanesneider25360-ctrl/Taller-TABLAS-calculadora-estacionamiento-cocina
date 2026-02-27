# Clases

class Ingrediente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = 100
        self.procesado = False

    def recibir_corte(self, dano):
        self.vida -= dano
        if self.vida <= 0:
            self.vida = 0
            self.procesado = True
            print(f"{self.nombre} está completamente picado ")


class Cuchillo:
    def __init__(self):
        self.filo = 100

    def cortar(self, ingrediente):
        if self.filo <= 0:
            print(" El cuchillo está sin filo. Debes afilar.")
            return

        print(f"Cortando {ingrediente.nombre}...")
        ingrediente.recibir_corte(25)
        self.filo -= 20
        print(f"Filo restante: {self.filo}%")

    def afilar(self):
        self.filo = 100
        print(" Cuchillo afilado al 100%")


class Olla:
    def __init__(self):
        self.contenido = []
        self.coccion = 0

    def agregar(self, ingrediente):
        if ingrediente.procesado:
            self.contenido.append(ingrediente.nombre)
            print(f"{ingrediente.nombre} agregado a la olla ")
        else:
            print(f"{ingrediente.nombre} aún no está listo.")

    def hervir(self):
        while self.coccion < 100:
            opcion = input("¿Deseas seguir hirviendo? (s/n): ").lower()
            if opcion != "s":
                break

            self.coccion += 20
            print(f"Cocción actual: {self.coccion}%")

        if self.coccion >= 100:
            print("\n ¡Combate culinario finalizado!")
            print("La pasta ha sido servida con éxito ")
