# ========= Clase Parqueadero =========
from usuario_carro import Usuario, Carro
from clase_registro import Registro


class Parqueadero:
    def __init__(self):
        self.registros = []

    def agregar_registro(self):
        print("\n--- INGRESAR DATOS ---")

        # Datos usuario
        cedula = input("Cedula: ")
        nombre = input("Nombre: ")
        tipo_usuario = input("Tipo usuario: ")

        # Datos carro
        placa = input("Placa carro: ")
        tipo_carro = input("Tipo carro: ")
        color = input("Color carro: ")

        # Datos registro
        puesto = input("Puesto: ")
        fecha = input("Fecha: ")
        hora_entrada = input("Hora entrada: ")
        hora_salida = input("Hora salida (si no hay deje vacío): ")
        estado = input("Estado (Entrada/Salida): ")

        usuario = Usuario(cedula, nombre, tipo_usuario)
        carro = Carro(placa, tipo_carro, color)

        registro = Registro(usuario, carro, puesto,
                            fecha, hora_entrada,
                            hora_salida, estado)

        self.registros.append(registro)
        print(" Registro guardado")

    def mostrar_registros(self):
        print("\n===== REGISTROS =====\n")
        for r in self.registros:
            r.mostrar()