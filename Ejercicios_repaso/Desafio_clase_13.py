

class ListaAtletas:
    
    def __init__(self):
        self.lista = []
        
    def agregar_atleta(self, atleta):
        self.lista.append(atleta)
        
    def mostrar_atletas(self, atleta):
        for atleta in self.lista:
            print(atleta.nombre)
            
    def mostrar_imc_atletas(self):
        for atleta in self.lista:
            atleta.calcular_imc()
            print(atleta.nombre, atleta.getImc())


class Atleta:
    
    def __init__(self, altura:float, peso:float, **kwargs) -> None: #Le pasas los atributos que queres obligatorio     
        self.nombre = kwargs.get('nombre', '')
        self.apellido = kwargs.get('apellido', '')
        self.altura = altura #Y no se le pone ningun valor por default porque es obligatorio
        self.peso = peso #Elijo estos dos obligatorios porque son lo que necesito para hacer el calculo de imc
        self.telefono = kwargs.get('telefono', '')
        self.__imc = '' #Esto se debe calcular por eso no puede venir como argumento
        

    def calcular_imc(self):
        resultado = self.peso / self.altura**2

        if resultado < 18.5:
            self.__imc = 'Peso inferior'
        elif 18.5 <= resultado < 24.9:
            self.__imc = 'Normal'
        elif 24.9 <= resultado < 29.9:
            self.__imc = 'Sobrepeso'
        elif 29.9 <= resultado < 34.9:
            self.__imc = 'Obesidad'
        else:
            self.__imc = 'Obesidad extrema'
            
    
    def getImc(self):
        return self.__imc
    
    def setImc(self, valor):
        self.calcular_imc()
         
    
listaAtletas = ListaAtletas()
atleta = Atleta(1.82, 84)

listaAtletas.agregar_atleta(atleta)
atleta.calcular_imc()

print(atleta.getImc())
listaAtletas.mostrar_imc_atletas()