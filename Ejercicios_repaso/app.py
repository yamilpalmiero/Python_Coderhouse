import sys  

if len(sys.argv) == 2:
    
    argumentos = int(sys.argv[1])
    
    for i in range(11):
        print(f'{argumentos} x {i} = {argumentos * i}')
    
else:
    print('Faltan argumentos!')
    print('Uso: app.py <numero>')