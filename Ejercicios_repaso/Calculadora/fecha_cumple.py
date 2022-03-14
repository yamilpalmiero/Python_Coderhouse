from datetime import datetime, timedelta

fecha_hoy = datetime.now()
fecha_nacimiento = datetime(1988,5,1,0,0)

resultado = fecha_hoy - fecha_nacimiento
print(f'Hace {resultado} que nací.')