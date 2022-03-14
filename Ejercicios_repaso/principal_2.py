from Calculadora.funciones_calculadora import sumar
from Calculadora.print_formulas import print_formaula

print('PROGRAMA PRINCIPAL')

resultado = sumar(2,3)
print(resultado)

resultado_str = print_formaula(2,3,'+')
print(resultado_str)