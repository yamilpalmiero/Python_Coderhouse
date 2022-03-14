#import funciones_calculadora as calcu
#from funciones_calculadora import sumar, restar
from Calculadora.funciones_calculadora import *
from Clases import Persona

#resultado = calcu.sumar(2,3)
#resultado = restar(5,2)
resultado = restar(5,2)
print(resultado)

persona_5 = Persona('Yamil', 337822333, 33)
persona_5.hablar('Hola que onda')
