# FUNCIONES

def imprimir_menu():

    print('********** MENU **********')
    print('1. Agregar materia.')
    print('2. Conocer estado de na materia.')
    print('3. Salir.')


def solicitar_datos():
    materia = input('Ingrese materia: ')
    calificaiones = input('Ingrese calificaciones separadas por coma: ')

    calificaciones = calificaciones.split(',')

    return materia, calificaciones


def agregar_materia(materia, calificaciones):
    archivo = open(
        r'logyt@logyt-ThinkPad-T440p:~/Escritorio/Python/Repaso/misCalificaciones.txt', 'w')

    cadena = materia+','+','.join(calificaciones)+'\n'

    archivo.write(cadena)
    archivo.close()


def estado_materia(nombre):
    archivo = open(
        r'logyt@logyt-ThinkPad-T440p:~/Escritorio/Python/Repaso/misCalificaiones.txt', 'r')

    for linea in archivo.readlines():
        listado = linea.split(',')
        materia = listado[0]
        calificaciones = listado[1:]

        if materia.lower() == nombre.lower():

            acumulador = 0

            for calificacion in calificaciones:
                calificacion = float(calificacion)
                acumulador += calificacion

            promedio = acumulador/len(calificaciones)

            if promedio >= 6:
                print('Aprobado')
            else:
                print('Desaprobado')
            
            archivo.close()
            return
        
    archivo.close()


imprimir_menu()
opcion = input('Ingrese opcion: ')

while opcion != 3:
    if opcion == '1':
        materia, calificaciones = solicitar_datos()
        agregar_materia(materia, calificaciones)
    elif opcion == '2':
        materia=input('Ingrese materia: ')
    
    imprimir_menu()
    opcion = input('Ingrese opcion: ')
