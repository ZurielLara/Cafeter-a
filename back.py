class Valores():
    def __init__(self):
        self._tipoCafe = []
        self._sabor = []
        self._tamanio = []
        self._tipoLeche = []
        self._extras = []
        self._tipoPedido = []
    
    def tipoCafe(self):
        self._tipoCafe = ['Frío', 'Caliente']
        return self._tipoCafe

    def sabor(self):
        self._sabor = ['    Cappuchino', '    Mocca']
        return self._sabor

    def tamanio(self):
        self._tamanio = ['    Chico', '    Mediano', '   Grande']
        return self._tamanio

    def tipoLeche(self):
        self._tipoLeche = ['    Entera', '    Deslactosada', '    Coco', '    Almendras']
        return self._tipoLeche

    def extras(self):
        self._extras = ['    cup holder']
        return self._extras

    def tipoPedido(self):
        self._tipoPedido = ['    Consumo Local', '    Para Llevar']
        return self._tipoPedido


class Ventas():
    def __init__(self):
        self._horas = []
        self._ventasH = []
        self._semanas = []
        self._ventasM = []

    def ventasD(self):
        self._horas = [ 13 , 14, 16]
        self._ventasH = [3, 2, 4]
        
        return self._horas, self._ventasH

    def ventasM(self):
        self._semanas = [1, 2, 3, 4]
        self._ventasM = [12, 20, 10, 5]

        return self._semanas, self._ventasM, len(self._semanas)


class Login():

    def __init__(self):
        #self.conexion = myslq.conector.connect(host='localhost',
        #                                        database='base_datos',
        #                                        user='root',
        #                                        password='admin'
        #                                        )
        pass
    
    def busca_users(self, users):
        #cur=self.conexion.cursor()
        #sql = "SELECT * FROM login_datos WHERE Users= {}".format(users)
        #cur.execute(slq)
        #usersx = cur.fetchall()
        #cur.close()
        admin = "zuriel"
        if users.lower() == admin:
            return True
        else: 
            return False

    def busca_password(self, password):
        #cur=self.conexion.cursor()
        #sql = "SELECT * FROM login_datos WHERE Password= {}".format(password)
        #cur.execute(slq)
        #passwordx = cur.fetchall()
        #cur.close()
        contra = "admin"
        if password.lower() == contra:
            return True
        else:
            return False


valores = Valores()
