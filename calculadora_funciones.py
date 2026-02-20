class Calculadora:

    def __init__ (self, dato_fecha):
        self.fecha = dato_fecha
        self.resultado = ""
        self.tipo_operacion = ""
# GET _____________________________________________________

    def get_fecha(self):
        return self.fecha
    
    def get_resultado(self):
        return self.resultado
    
    def get_tipo_operacion(self):
        return self.tipo_operacion
    
# SET
    
    def set_fecha(self,nueva_fecha):
        self.fecha = nueva_fecha

    def set_tipo_operacion(self,nuevo_tipo_op):
        self.tipo_operacion = nuevo_tipo_op

# OPERACIONES _________________________________________________

    def Hacer_suma(self,obj_numero,obj_numero_2):
        self.resultado = obj_numero.get_numero()+obj_numero_2.get_numero()
        print(f"la suma es: {self.resultado}")
    
    def Hacer_resta(self,obj_numero,obj_numero_2):
        self.resultado = obj_numero.get_numero()-obj_numero_2.get_numero()
        print(f"la resta es: {self.resultado}")
    
    def Hacer_division(self, obj_numero, obj_numero_2):
        self.resultado = obj_numero.get_numero()/obj_numero_2.get_numero()
        print(f"el resultado de la division es: {self.resultado}")

    def Hacer_multiplicacion(self,obj_numero, obj_numero_2):
        self.resultado = obj_numero.get_numero()* obj_numero_2.get_numero()
        print(f"el resultado de la multiplicacion es: {self.resultado}")
#________________________________________________________________

    tabla = []
    def Guardar_info_tabla(self):
        print("---Elije una operacion:---\n")
        print(" Opcion (1): Sumar. \n Opcion (2): Restar. \n Opcion (3): Dividir. \n Opcion (4): Multiplicar. \n")
        opcion = int(input("Seleccione opción: "))

        if opcion == 1:
            self.Hacer_suma
            print(f"{self.get_resultado}")
        elif opcion == 2:
            self.Hacer_resta
        elif opcion == 3:
            self.Hacer_division
        elif opcion == 4:
            self.Hacer_multiplicacion
        else:
            print("Error, nomuero no valido.")