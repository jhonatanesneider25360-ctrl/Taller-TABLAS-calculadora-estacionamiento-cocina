from calculadora_funciones import Calculadora
from numeros import Numeros
from usuario import Usuario

obj_usuario = Usuario()
obj_usuario.set_nombre("Jhonatan")
obj_usuario.set_apellido("Garcia")
obj_usuario.set_cedula("1094221518")

obj_numero = Numeros()
obj_numero.set_numero(2)

obj_numero_2 = Numeros()
obj_numero_2.set_numero(4)

# ________________________________________________________________________

obj_calculadora = Calculadora("20/02/2026")

obj_calculadora.Hacer_suma(obj_numero,obj_numero_2)
obj_calculadora.Hacer_resta(obj_numero,obj_numero_2)
obj_calculadora.Hacer_division(obj_numero,obj_numero_2)
obj_calculadora.Hacer_multiplicacion(obj_numero,obj_numero_2)

dato = obj_calculadora.get_resultado()
# _______________________________________
obj_calculadora.Guardar_info_tabla()



