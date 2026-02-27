# ========= Clase Registro =========
class Registro:
    def __init__(self, usuario, carro, puesto,
                 fecha, hora_entrada, hora_salida, estado):

        self.usuario = usuario
        self.carro = carro
        self.puesto = puesto
        self.fecha = fecha
        self.hora_entrada = hora_entrada
        self.hora_salida = hora_salida
        self.estado = estado

    def mostrar(self):
        print(f"{self.usuario.cedula} | {self.usuario.nombre} | "
              f"{self.usuario.tipo} | {self.carro.placa} | "
              f"{self.carro.tipo} | {self.carro.color} | "
              f"{self.puesto} | {self.fecha} | "
              f"{self.hora_entrada} | {self.hora_salida} | "
              f"{self.estado}")