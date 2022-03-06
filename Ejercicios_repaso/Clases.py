class Persona:

  #Atributos de clase
  especie='mamifero'
  brazos=2

  #Ctor
  def __init__(self, nombre, dni, edad):

    #Atributos de instancia
    self.nombre=nombre
    self.dni=dni
    self.edad=edad

  def getEspecie(self, especie, brazos):
    print(f'Es un {self.especie} y tiene {self.brazos} brazos.')

  def getDatos(self):
    print(f'\nNombre: {self.nombre}\nDNI: {self.dni}\nEdad: {self.edad} años\n')

  def __str__(self):
    return f'{self.nombre}, {self.edad}'


persona_1=Persona('Yamil', 33782264, 33)
persona_2=Persona('Mariana', 35189411, 31)

persona_1.getEspecie(Persona.especie, Persona.brazos)
persona_2.getDatos()

print(persona_1)#Esto es posible gracias al metodo str