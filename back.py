class Valores():
    def __init__(self):
        self.tipo_Cafe = []
        self._sabor = []
        self._tamanio = []
    
    def tipoCafe(self):
        self.tipo_Cafe = ['Frío', 'Caliente']
        return self.tipo_Cafe

    def sabor(self):
        self._sabor = ['Cappuchino', 'Mocca']
        return self._sabor

    def tamanio(self):
        self._tamanio = ['Chico', 'Mediano', 'Grande']
        return self._tamanio

valores = Valores()
