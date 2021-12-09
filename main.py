from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import pyqtgraph as pg
from back import Valores as val
from back import Ventas as ven
from back import Login as lg
from operator import xor
import sys


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(480, 581)
        self.centralwidget = QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setGeometry(QRect(0, 0, 480, 540))
        self.label_4.setAutoFillBackground(True)
        self.label_4.setText("")
        self.label_4.setPixmap(QPixmap("./Recursos/Imagenes/bgLogin.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setGeometry(QRect(60, 10, 360, 120))
        self.label_5.setStyleSheet("background-color:rgb(126, 110, 109);\n"
        "font: 48pt \"Vladimir Script\";\n"
        "border-radius: 10px;\n"
        "border: 5px soild #000000;")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.users = QLineEdit(self.centralwidget)
        self.users.setGeometry(QRect(100, 180, 280, 40))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.users.setFont(font)
        self.users.setStyleSheet("background:rgb(255, 219, 167);\n"
        "border-radius: 10px;\n"
        "Border:None;")
        self.users.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.users.setObjectName("users")
        self.password = QLineEdit(self.centralwidget)
        self.password.setGeometry(QRect(100, 280, 280, 40))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.password.setFont(font)
        self.password.setStyleSheet("background:rgb(255, 219, 167);\n"
        "border-radius: 10px;\n"
        "Border:None;")
        self.password.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.password.setObjectName("password")
        self.usuario_incorrecto = QLabel(self.centralwidget)
        self.usuario_incorrecto.setGeometry(QRect(100, 220, 180, 30))
        self.usuario_incorrecto.setStyleSheet("background-color: rgba(0, 0, 0 , 0%);\n"
        "font: 10pt \"Arial\";\n"
        "color:rgb(255, 0, 0);\n"
        "border:none;")
        self.usuario_incorrecto.setText("")
        self.usuario_incorrecto.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.usuario_incorrecto.setFixedWidth(300)
        self.usuario_incorrecto.setObjectName("usuario_incorrecto")
        self.contrasena_incorrecta = QLabel(self.centralwidget)
        self.contrasena_incorrecta.setGeometry(QRect(160, 320, 171, 51))
        self.contrasena_incorrecta.setStyleSheet("background-color: rgba(0, 0, 0 , 0%);\n"
        "font: 10pt \"Arial\";\n"
        "color:rgb(255, 0, 0);\n"
        "border:none;")
        self.contrasena_incorrecta.setText("")
        self.contrasena_incorrecta.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.contrasena_incorrecta.setObjectName("contrasena_incorrecta")
        self.bt_ingresar = QPushButton(self.centralwidget)
        self.bt_ingresar.setGeometry(QRect(195, 370, 90, 30))
        self.bt_ingresar.setStyleSheet("QPushButton{\n"
        "    \n"
        "        background-color:rgb(126, 110, 109);\n"
        "        font: 8pt \"MS Shell Dlg 2\";\n"
        "        color:rgb(255, 255, 255);\n"
        "        border-radius: 15px;\n"
        "border:1px soild #00007f;\n"
        "\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "    \n"
        "        background-color:rgb(67, 42, 37);\n"
        "        font: 8pt \"MS Shell Dlg 2\";\n"
        "        border-radius: 15px;\n"
        "border:1px soild #00007f;\n"
        "\n"
        "}\n"
        "")
        self.bt_ingresar.setObjectName("bt_ingresar")
        self.bt_ingresar.clicked.connect(self.iniciarSesion)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setGeometry(QRect(160, 140, 160, 40))
        self.label_6.setStyleSheet("background-color: rgba(0, 0, 0 , 0%);\n"
        "font: 12pt \"Arial\";\n"
        "color:rgb(255, 255, 255);\n"
        "border:none;")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setGeometry(QRect(160, 240, 160, 40))
        self.label_3.setStyleSheet("background-color: rgba(0, 0, 0 , 0%);\n"
        "font: 12pt \"Arial\";\n"
        "color:rgb(255, 255, 255);\n"
        "border:none;")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        Login.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Login)
        self.menubar.setGeometry(QRect(0, 0, 480, 21))
        self.menubar.setObjectName("menubar")
        Login.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Login)
        self.statusbar.setObjectName("statusbar")
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)
        QMetaObject.connectSlotsByName(Login)

    def iniciarSesion(self):
        self.contrasena = self.password.text()
        self.usuarios = self.users.text()

        if lg.busca_users(self, self.usuarios) and lg.busca_password(self, self.contrasena):
            self.w = Window()
            self.w.show()
            self.hide()
        else:
            self.usuario_incorrecto.setText('El usuario o la contraseña son incorrectos')

    def retranslateUi(self, Login):
        _translate = QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "MainWindow"))
        self.label_5.setText(_translate("Login", "Iniciar Sesión"))
        self.users.setPlaceholderText(_translate("Login", "Ingrese su usuario"))
        self.password.setPlaceholderText(_translate("Login", "Ingrese su su contraseña"))
        self.bt_ingresar.setText(_translate("Login", "Continuar"))
        self.label_6.setText(_translate("Login", "Usuario"))
        self.label_3.setText(_translate("Login", "Contraseña"))

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.tipoCafe = valores.tipoCafe()
        self.sabor = valores.sabor()
        self.tamanio = valores.tamanio()
        self.tipoLeche = valores.tipoLeche()
        self.extras = valores.extras()
        self.tipoPedido = valores.tipoPedido()
        self.horas, self.ventasH = ven.ventasD(self)
        self.filasVentasDia = len(self.horas)
        self.semanas, self.ventasM, self.filasVentasMes = ven.ventasM(self)
        self.anchoWPedido = 180
        self.largoWPedido = 70

        # ------ VENTANA PRINCIPAL ------
        # Modificación de las propiedades
        self.setWindowTitle('Cafeteria') # Título de la ventana
        self.setStyleSheet('background-color: white;') # Color de fondo
        self.Width = 800 # Ancho
        self.height = int(0.618 * self.Width) # Largo
        self.resize(self.Width, self.height) # Modificación del tamaño

        # ---- INICIALIZACION DE WIDGETS ----
        # Fuentes
        self.negrita14 = QFont('Arial', 14)
        self.fuenteNegrita10 = QFont('Arial', 10)
        self.fuenteCursiva = QFont('Arial', 20, 10, True)
        self.negrita14.setBold(True)
        self.fuenteNegrita10.setBold(True)

        # Botones
        self.btnPedidos = QPushButton('Pedido') # Botón Pedido
        self.btnInventario = QPushButton('Inventario') # Botón Inventario
        self.btnVentas = QPushButton('Ventas') # Botón Ventas
        self.btnFinalizarP = QPushButton('Finalizar Pedido', objectName = 'btnFinalizarP')  # Botón Finalizar
        self.btnAgregarP = QPushButton('Agregar Pedido', objectName = 'btnAgregarP')
        
        # Combo box
        self.btnTipoCafe = QComboBox(objectName = 'btnTipoCafe') # Menú desplegable "Tipo de Café"
        self.btnSabor = QComboBox(objectName = 'btnSabor') # Menú desplegable "Sabor"
        self.btnTamanio = QComboBox(objectName = 'btnTamanio') # Menú desplegable "Tamaño"
        self.btnTipoLeche = QComboBox(objectName = 'btnTipoLeche') # Menú desplegable "Tipo de Leche"
        self.btnExtras = QComboBox(objectName = 'btnExtras') # Menú desplegable "Extras"
        self.btnTipoPedido = QComboBox(objectName = 'btnTipoPedido') # Menú desplegable "Tipo de Pedido"

        # Campos de texto
        self.cNombreCliente = QLineEdit(objectName = 'cNombreCliente') # Campo de texto "Nombre del cliente"
        self.cNombreCliente.setPlaceholderText('Nombre del cliente')

        #Etiquetas
        self.logoCafe = QLabel('') # Logo del Café
        self.pedidoLabel = QLabel('Pedidos')
        self.inventarioLabel = QLabel('Inventario')
        self.ventasLabel = QLabel('Ventas')
        self.ventasDiaL = QLabel('Ventas por día')
        self.ventasMesL = QLabel('Ventas por mes')
        self.pixmapCafe = QPixmap('./Recursos/Imagenes/logoCafe.png')
        self.pixmapCafe.scaled(20, 20)
        self.logoCafe.setPixmap(self.pixmapCafe)
        self.pedidoLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Items de Combobox
        self.btnTipoCafe.addItem('Tipo de Café')
        self.btnTipoCafe.addItems(self.tipoCafe)
        self.btnSabor.addItem('Sabor')
        self.btnSabor.addItems(self.sabor)
        self.btnTamanio.addItem('Tamaño')
        self.btnTamanio.addItems(self.tamanio)
        self.btnTipoLeche.addItem('Tipo de Leche')
        self.btnTipoLeche.addItems(self.tipoLeche)
        self.btnExtras.addItem('Extras')
        self.btnExtras.addItems(self.extras)
        self.btnTipoPedido.addItem('Tipo de Pedido')
        self.btnTipoPedido.addItems(self.tipoPedido)

        # Desactivando Items de QComboBox
        self.btnTipoCafe.model().item(0).setEnabled(False)
        self.btnSabor.model().item(0).setEnabled(False)
        self.btnTamanio.model().item(0).setEnabled(False)
        self.btnTipoLeche.model().item(0).setEnabled(False)
        self.btnExtras.model().item(0).setEnabled(False)
        self.btnTipoPedido.model().item(0).setEnabled(False)

        # Tablas
        self.tablaInventario = QTableWidget(2, 6)
        self.tablaVentasDia = QTableWidget(self.filasVentasDia, 2)
        self.tablaVentasMes = QTableWidget(self.filasVentasMes, 2)

        # ESTTILOS
        # Hojas de Estilos
        self.btnPedidos.setStyleSheet('border: none; color: white;')
        self.btnInventario.setStyleSheet('border: none; color: white;')
        self.btnVentas.setStyleSheet('border: none; color: white;')
        self.pedidoSS = """
                            QComboBox { 
                                        border-radius: 10px; 
                                        color: white;
                                        }

                            QLineEdit {
                                    border: 1px solid brown;
                                    border-radius: 5px;
                                    background-color: brown;
                                    color: white;
                                    }

                            QPushButton {
                                    border: 1px solid brown;
                                    border-radius: 5px;
                                    background-color: brown;
                                    color: white;
                            }
                            
                            QComboBox#btnTipoCafe {
                                background-color: rgb(255, 87, 87); 
                            }
                            
                            QComboBox#btnSabor {
                                background-color: rgb(228, 194, 20); 
                            }

                            QComboBox#btnTamanio {
                                background-color: rgb(255, 22, 22); 
                            }
                            
                            QComboBox#btnTipoLeche {
                                background-color: rgb(138, 189, 65); 
                            }
                            
                            QComboBox#btnExtras {
                                background-color: rgb(140, 82, 255); 
                            }

                            QComboBox#btnTipoPedido {
                                background-color: rgb(63, 223, 194); 
                            }

                            QPushButton#btnFinalizarP {
                                background-color: rgb(150, 22, 22);
                            }

                            QPushButton#btnAgregarP {
                                background-color: rgb(150, 22, 22);
                            }
                                """
        self.tablaInventario.setStyleSheet('border: none;')

        # Configuración de Fuentes de los Widgets
        self.btnPedidos.setFont(self.negrita14) # -> Inicia Conf. QPushButton
        self.btnInventario.setFont(self.negrita14)
        self.btnVentas.setFont(self.negrita14)
        self.btnFinalizarP.setFont(self.negrita14) 
        self.btnAgregarP.setFont(self.negrita14) # <- Termina Conf. QPushButton
        self.btnTipoCafe.setFont(self.negrita14) # -> Inicia Conf. QComboBox
        self.btnSabor.setFont(self.negrita14)
        self.btnTamanio.setFont(self.negrita14)
        self.btnTipoLeche.setFont(self.negrita14)
        self.btnExtras.setFont(self.negrita14)
        self.btnTipoPedido.setFont(self.negrita14)
        self.cNombreCliente.setFont(self.negrita14) # <- Termina Conf. QComboBox
        self.pedidoLabel.setFont(self.fuenteCursiva) # -> Inicia Conf. QLabel
        self.ventasLabel.setFont(self.fuenteCursiva)
        self.ventasDiaL.setFont(self.negrita14)
        self.ventasMesL.setFont(self.negrita14)
        self.inventarioLabel.setFont(self.fuenteCursiva) # -> Termina Conf. QLablel

        #Configuración de tamaño de ls Widgets
        self.btnPedidos.setFixedSize(260, 50) # -> Inicia Conf. QPushButton
        self.btnInventario.setFixedSize(260, 50)
        self.btnVentas.setFixedSize(260, 50)
        self.btnFinalizarP.setFixedSize(self.anchoWPedido, self.largoWPedido)
        self.btnAgregarP.setFixedSize(self.anchoWPedido, self.largoWPedido) # <- Termina Conf. QPushButton
        self.btnTipoCafe.setFixedSize(self.anchoWPedido, self.largoWPedido) # -> Inicia conf. QComboBox
        self.btnSabor.setFixedSize(self.anchoWPedido, self.largoWPedido)
        self.btnTamanio.setFixedSize(self.anchoWPedido, self.largoWPedido)
        self.btnTipoLeche.setFixedSize(self.anchoWPedido, self.largoWPedido)
        self.btnExtras.setFixedSize(self.anchoWPedido, self.largoWPedido)
        self.btnTipoPedido.setFixedSize(self.anchoWPedido, self.largoWPedido)
        self.cNombreCliente.setFixedSize(self.anchoWPedido, self.largoWPedido) # <- Termina Conf. QComboBox
        self.logoCafe.setFixedSize(260, 200) # -> Inicia Conf. QLabel
        self.pedidoLabel.setFixedSize(1290, 100)
        self.tablaInventario.setFixedSize(1260, 200) # <- Termina Conf. QLabel

        # Alineación
        self.inventarioLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ventasLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #Configuración de iconos
        self.btnPedidos.setIcon(QIcon('./Recursos/Iconos/tCafe.png'))
        self.btnInventario.setIcon(QIcon('./Recursos/Iconos/inventario.png'))
        self.btnVentas.setIcon(QIcon('./Recursos/Iconos/ventas.png'))
        self.btnPedidos.setIconSize(QSize(35, 35))
        self.btnInventario.setIconSize(QSize(35, 35))
        self.btnVentas.setIconSize(QSize(35, 35))

        # Opciones para tablas
        self.tablaInventario.setHorizontalHeaderLabels(['ID', 'Nombre del producto', 'Categoría', 'Ubicación', 'Cantidad', 'Costo unitario'])
        self.tablaVentasDia.setHorizontalHeaderLabels(['Horas', 'Número de ventas'])
        self.tablaVentasMes.setHorizontalHeaderLabels(['Semana', 'Número de ventas'])
        self.tablaInventario.resizeColumnsToContents()
        self.tablaVentasDia.resizeColumnsToContents()
        self.tablaVentasMes.resizeColumnsToContents()
        self.tablaInventario.resizeRowsToContents()
        self.tablaVentasDia.resizeRowsToContents()
        self.tablaVentasMes.resizeRowsToContents()

        # Manejadores de eventos para páginas
        self.btnPedidos.clicked.connect(self.botonPedidos)
        self.btnInventario.clicked.connect(self.botonInventario)
        self.btnVentas.clicked.connect(self.botonVentas)

        # Pestañas
        self.tab1 = self.ventanaPedidos()
        self.tab2 = self.ventanaInventario()
        self.tab3 = self.ventanaVentas()

        self.principal() # Se llama a la pestaña principal
        self.showMaximized() # Despliega "maximizada la pantalla principal"

    def principal(self):
        left_layout = QVBoxLayout() # Layout Vertical
        left_layout.addWidget(self.logoCafe) # Imagen del logo del café
        left_layout.addSpacerItem(QSpacerItem(260, 15))
        left_layout.addWidget(self.btnPedidos) # Botón para página Pedidos
        left_layout.addWidget(self.btnInventario) # Botón para página inventario
        left_layout.addWidget(self.btnVentas) # Botón para página ventas
        left_layout.addStretch(5) # Alineado desde bottom a top
        left_widget = QWidget() # Intancia de la clase QWidget
        left_widget.setStyleSheet('background-color: brown;')
        left_widget.setFixedWidth(260)
        left_widget.setLayout(left_layout) # Se define el layout del documento

        self.right_widget = QTabWidget() 
        self.right_widget.tabBar().setObjectName("mainTab")

        self.right_widget.addTab(self.tab1, '')
        self.right_widget.addTab(self.tab2, '')
        self.right_widget.addTab(self.tab3, '')

        self.right_widget.setCurrentIndex(0)
        self.right_widget.setStyleSheet('''QTabBar::tab{width: 0; \
            height: 0; margin: 0; padding: 0; border: none; background-color: red}''')

        main_layout = QHBoxLayout()
        main_layout.addWidget(left_widget)
        main_layout.addWidget(self.right_widget)
        main_layout.setStretch(0, 40)
        main_layout.setStretch(1, 200)
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    # Botones
    def botonPedidos(self):
        self.right_widget.setCurrentIndex(0)
        self.btnPedidos.setStyleSheet('background-color: red; border: none; color: white;')
        self.btnInventario.setStyleSheet('background-color: brown; border: none; color: white;')
        self.btnVentas.setStyleSheet('background-color: brown; border: none; color: white;')

    def botonInventario(self):
        self.right_widget.setCurrentIndex(1)
        self.btnPedidos.setStyleSheet('background-color: brown; border: none; color: white;')
        self.btnInventario.setStyleSheet('background-color: red; border: none; color: white;')
        self.btnVentas.setStyleSheet('background-color: brown; border: none; color: white;')

    def botonVentas(self):
        self.right_widget.setCurrentIndex(2)
        self.btnPedidos.setStyleSheet('background-color: brown; border: none; color: white;')
        self.btnInventario.setStyleSheet('background-color: brown; border: none; color: white;')
        self.btnVentas.setStyleSheet('background-color: red; border: none; color: white;')
	
    # Páginas
    def ventanaPedidos(self):
        main_layout = QVBoxLayout()
        hbox = QHBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()

        hbox.addWidget(self.btnTipoCafe)
        hbox.addWidget(self.btnSabor)
        hbox.addWidget(self.btnTamanio)
        
        hbox1.addWidget(self.btnTipoLeche)
        hbox1.addWidget(self.btnExtras)
        hbox1.addWidget(self.btnTipoPedido)
        
        hbox2.addWidget(self.cNombreCliente)
        hbox2.addWidget(self.btnAgregarP)
        hbox2.addWidget(self.btnFinalizarP)
        
        main_layout.addWidget(self.pedidoLabel)
        main_layout.addLayout(hbox3)
        main_layout.addLayout(hbox)
        main_layout.addLayout(hbox1)
        main_layout.addLayout(hbox2)

        main = QWidget()
        main.setStyleSheet(self.pedidoSS)
        main.setLayout(main_layout)
        return main

    def ventanaInventario(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.inventarioLabel)
        main_layout.addSpacerItem(QSpacerItem(10, 100))
        main_layout.addWidget(self.tablaInventario)
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main
        
    def ventanaVentas(self):
        for i in range(0, len(self.horas)):
            self.tablaVentasDia.setItem(i, 0, QTableWidgetItem(str(self.horas[i])))
            self.tablaVentasDia.setItem(i, 1, QTableWidgetItem(str(self.ventasH[i])))
            
        main_layout = QVBoxLayout()
        vbox = QVBoxLayout()
        vbox1 = QVBoxLayout()
        hbox = QHBoxLayout()

        vbox.addWidget(self.ventasDiaL)
        vbox.addWidget(self.tablaVentasDia)

        vbox1.addWidget(self.ventasMesL)
        vbox1.addWidget(self.tablaVentasMes)

        hbox.addLayout(vbox)
        hbox.addLayout(vbox1)

        main_layout.addWidget(self.ventasLabel)
        main_layout.addLayout(hbox)
        main = QWidget()
        main.setLayout(main_layout)
        return main


if __name__ == '__main__':

    app = QApplication(sys.argv)
    Login = QMainWindow()
    valores = val()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec())
