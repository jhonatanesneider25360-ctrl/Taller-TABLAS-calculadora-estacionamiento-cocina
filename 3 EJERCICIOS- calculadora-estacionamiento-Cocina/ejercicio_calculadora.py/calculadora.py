from registro import Registro

class Calculadora:
    """
    Maneja la lógica de las operaciones y el historial de registros.
    Importa la clase Registro para crear nuevos objetos de historial.
    """
    def __init__(self):
        self.historial = []

    def calcular(self, usuario, a, b, tipo):
        if tipo == "suma":
            resultado = a + b
        elif tipo == "resta":
            resultado = a - b
        elif tipo == "multiplicacion":
            resultado = a * b
        elif tipo == "division":
            if b == 0:
                print("\n[!] Error: No se puede dividir por cero.")
                return None
            resultado = a / b
        else:
            return None

        # Creamos el objeto Registro e indicamos que este registro pertenece a este usuario
        nuevo_registro = Registro(usuario, a, b, tipo, resultado)
        self.historial.append(nuevo_registro)
        return resultado

    def imprimir_tabla(self):
        # 1. Verificamos si la lista está vacía de forma simple
        if len(self.historial) == 0:
            print("\n[!] No hay nada que mostrar en el historial.")
            return

        # 2. Imprimimos una línea decorativa y los encabezados de forma manual
        print("\n" + "=" * 110)
        print("NOMBRE".ljust(20) + "| CEDULA".ljust(15) + "| OP".ljust(12) + "| NUM1".ljust(8) + "| NUM2".ljust(8) + "| RESULTADO".ljust(12) + "| FECHA")
        print("-" * 110)

        # 3. Recorremos el historial y accedemos a cada atributo directamente
        for r in self.historial:
            # Usamos .ljust() para dar espacios a la derecha y que todo quede alineado
            nombre = str(r.nombre_u).ljust(20)
            cedula = str(r.cedula_u).ljust(14)
            operacion = str(r.tipo_op).ljust(11)
            n1 = str(r.num1).ljust(7)
            n2 = str(r.num2).ljust(7)
            resultado = str(r.res).ljust(11)
            fecha = str(r.fecha)

            # Imprimimos la fila uniendo los datos (incluyendo la fecha ahora)
            print(f"{nombre}| {cedula}| {operacion}| {n1}| {n2}| {resultado}| {fecha}")

        print("=" * 110 + "\n")
