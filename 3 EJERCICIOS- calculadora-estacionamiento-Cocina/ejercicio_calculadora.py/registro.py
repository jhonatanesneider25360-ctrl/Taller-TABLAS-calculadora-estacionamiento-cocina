import datetime

class Registro:
    """
    Representa un registro de una operación realizada.
    Toma un objeto de la clase Usuario para extraer sus datos.
    """
    def __init__(self, usuario, n1, n2, operacion, resultado):
        self.nombre_u = usuario.get_nombre()
        self.cedula_u = usuario.get_cedula()
        self.num1 = n1
        self.num2 = n2
        self.tipo_op = operacion
        self.res = resultado
        self.fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
