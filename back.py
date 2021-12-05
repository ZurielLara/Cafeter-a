class Valores():
    def __init__(self):
        self.tipo_Cafe = []
        self._sabor = []
        self._tamanio = []
        self._tipoLeche = []
        self._extras = []
        self._tipoPedido = []
    
    def tipoCafe(self):
        self.tipo_Cafe = ['Frío', 'Caliente']
        return self.tipo_Cafe

    def sabor(self):
        self._sabor = ['Cappuchino', 'Mocca']
        return self._sabor

    def tamanio(self):
        self._tamanio = ['Chico', 'Mediano', 'Grande']
        return self._tamanio

    def tipoLeche(self):
        self._tipoLeche = ['Entera', 'Deslactosada', 'Coco', 'Almendras']
        return self._tipoLeche

    def extras(self):
        self._extras = ['cup holder']
        return self._extras

    def tipoPedido(self):
        self._tipoPedido = ['Consumo Local', 'Para Llevar']
        return self._tipoPedido

valores = Valores()
