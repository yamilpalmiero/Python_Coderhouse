import sys

if len(sys.argv) == 3: #Son los dos argumentos más el nombre del script
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    
    if arg1.isdigit() and arg2.isdigit():
        arg1 = int(arg1)
        arg2 = int(arg2)  
           
        if 0<= arg1 <= 10 and 0<= arg2 <= 10:
            if arg1 >= 7 and arg2 >= 7:
                print('Promocionado')
            elif arg1 >= 4 and arg2 >= 4:
                print('Aprobado, debe rendir final')
            elif arg1 <= 4 or arg2 <= 4:
                if arg1 <= 4:
                    print('Desaprobado, recupera el primer parcial')
                else:
                    print('Desaprobado, debe rendir el segundo parcial')
            else:
                print('Desaprobado, recursa la materia')  
                      
    else:
        print('Debe indicar numeros.')   
        
else:
    print('Cantidad de argumentos incorrecta.')