from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from back import Valores as val
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.tipoCafe = valores.tipoCafe()
        self.sabor = valores.sabor()
        self.tamanio = valores.tamanio()

        # ------ VENTANA PRINCIPAL ------
        # Modificación de las propiedades
        self.setWindowTitle('Cafeteria') # Título de la ventana
        self.setStyleSheet('background-color: white;') # Color de fondo
        self.Width = 800 # Ancho
        self.height = int(0.618 * self.Width) # Largo
        self.resize(self.Width, self.height) # Modificación del tamaño
		
        # ---- INICIALIZACION DE WIDGETS ----
        # Botones
        self.btn_1 = QPushButton('Pedido', self) # Botón Pedido
        self.btn_2 = QPushButton('Inventario', self) # Botón Inventario
        self.btn_3 = QPushButton('Ventas', self) # Botón Ventas
        self.finalizarPedido = QPushButton('Finalizar', self)  # Botón Finalizar
        
        # Combo box
        self.btnTipoCafe = QComboBox() # Menú desplegable "Tipo de Café"
        self.btnSabor = QComboBox() # Menú desplegable "Sabor"
        self.btnTamanio = QComboBox() # Menú desplegable "Tamaño"
        self.btnTipoLeche = QComboBox() # Menú desplegable "Tipo de Leche"
        self.btnExtras = QComboBox() # Menú desplegable "Extras"
        self.btnTipoPedido = QComboBox() # Menú desplegable "Tipo de Pedido"

        # Campos de texto
        self.cNombreCliente = QLineEdit() # Campo de texto "Nombre del cliente"

        #Etiquetas
        self.logoCafe = QLabel('') # Logo del Café
        self.pixmapCafe = QPixmap('./Recursos/Imagenes/logoCafe.png')
        self.pixmapCafe.scaled(60, 60)
        self.logoCafe.setPixmap(self.pixmapCafe)

        # Opciones de Combobox
        self.btnTipoCafe.addItems(self.tipoCafe)
        self.btnSabor.addItems(self.sabor)
        self.btnTamanio.addItems(self.tamanio)

        # Estilos
        self.btn_1.setStyleSheet('border: none;')
        self.btn_2.setStyleSheet('border: none;')
        self.btn_3.setStyleSheet('border: none;')
        self.btnTipoCafe.setFixedSize(145, 55)
        self.btnSabor.setFixedSize(145, 55)
        self.btnTamanio.setFixedSize(145, 55)
        self.btnTipoLeche.setFixedSize(145, 55)
        self.btnExtras.setFixedSize(145, 55)
        self.btnTipoPedido.setFixedSize(145, 55)
        self.cNombreCliente.setFixedSize(200, 55)
        self.pedidoSS = """
                            QComboBox { 
                                        border-radius: 10px; 
                                        border: 1px solid brown;
                                        background-color: brown;
                                        color: white;
                                        }
                            QComboBox::down-arrow {
                                        border: none;
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
                                """

        # Manejadores de eventos para páginas
        self.btn_1.clicked.connect(self.button1)
        self.btn_2.clicked.connect(self.button2)
        self.btn_3.clicked.connect(self.button3)

        # Pestañas
        self.tab1 = self.ui1()
        self.tab2 = self.ui2()
        self.tab3 = self.ui3()

        self.initUI() # Se llama a la pestaña principal
        self.showMaximized() # Despliega "maximizada la pantalla principal"

    def initUI(self):
        left_layout = QVBoxLayout() # Layout Vertical
        left_layout.addWidget(self.logoCafe) # Imagen del logo del café
        left_layout.addWidget(self.btn_1) # Botón para página Pedidos
        left_layout.addWidget(self.btn_2) # Botón para página inventario
        left_layout.addWidget(self.btn_3) # Botón para página ventas
        left_layout.addStretch(5) # Alineado desde bottom a top
        left_layout.setSpacing(20) # Espaciado
        left_widget = QWidget() # Intancia de la clase QWidget
        left_widget.setStyleSheet("background-color: brown;") # Hoja de estilos del layout izquierdo
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
    def button1(self):
        self.right_widget.setCurrentIndex(0)
        self.btn_1.setStyleSheet('background-color: red; border: none;')
        self.btn_2.setStyleSheet('background-color: brown; border: none;')
        self.btn_3.setStyleSheet('background-color: brown; border: none;')

    def button2(self):
        self.right_widget.setCurrentIndex(1)
        self.btn_1.setStyleSheet('background-color: brown; border: none;')
        self.btn_2.setStyleSheet('background-color: red; border: none;')
        self.btn_3.setStyleSheet('background-color: brown; border: none;')

    def button3(self):
        self.right_widget.setCurrentIndex(2)
        self.btn_1.setStyleSheet('background-color: brown; border: none;')
        self.btn_2.setStyleSheet('background-color: brown; border: none;')
        self.btn_3.setStyleSheet('background-color: red; border: none;')
	
    # Páginas
    def ui1(self):
        main_layout = QVBoxLayout()
        hbox = QHBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()

        hbox.addWidget(self.btnTipoCafe)
        hbox.addWidget(self.btnSabor)
        hbox.addWidget(self.btnTamanio)
        
        hbox1.addWidget(self.btnTipoLeche)
        hbox1.addWidget(self.btnExtras)
        hbox1.addWidget(self.btnTipoPedido)
        
        hbox2.addWidget(self.cNombreCliente)
        hbox2.addWidget(self.finalizarPedido)
        
        main_layout.addLayout(hbox)
        main_layout.addLayout(hbox1)
        main_layout.addLayout(hbox2)

        main = QWidget()
        main.setStyleSheet(self.pedidoSS)
        main.setLayout(main_layout)
        return main

    def ui2(self):
        main_layout = QVBoxLayout()
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main
        
    def ui3(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('Ventas'))
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main


if __name__ == '__main__':
    app = QApplication(sys.argv)
    valores = val()
    ex = Window()
    ex.show()
    sys.exit(app.exec())
