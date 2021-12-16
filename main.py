from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from back import Valores
from back import Ventas as ven
from back import Login as lg
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
        self.tipoCafe = Valores.tipoCafe(self)
        self.sabor = Valores.sabor(self)
        self.tamanio = Valores.tamanio(self)
        self.tipoLeche = Valores.tipoLeche(self)
        self.extras = Valores.extras(self)
        self.tipoPedido = Valores.tipoPedido(self)
        self.horas, self.ventasH = ven.ventasD(self)
        self.filasVentasDia = len(self.horas)
        self.semanas, self.ventasM = ven.ventasM(self)
        self.filasVentasMes = len(self.semanas)
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
        self.btnAdminMatP = QPushButton('Admin. Materia Prima')
        self.btnAdminUsuarios = QPushButton('Admin. Usuarios')
        self.btnAdminProductos = QPushButton('Admin. Productos')
        self.btnFinalizarP = QPushButton('Finalizar Pedido', objectName = 'btnFinalizarP')  # Botón Finalizar
        self.btnAgregarP = QPushButton('Agregar Pedido', objectName = 'btnAgregarP')
        self.btnAgregar = QPushButton('Agregar', objectName = 'agregar')
        self.btnEliminar = QPushButton('Eliminar', objectName = 'eliminar')
        self.btnAceptar1 = QPushButton('Aceptar', objectName = 'btnAceptar1')
        self.btnAceptar2 = QPushButton('Aceptar', objectName = 'btnAceptar2')
        self.btnIngresar = QPushButton('Ingresar', objectName = 'btnIngresar')
        self.btnAgregarUser = QPushButton('Agregar', objectName = 'btnAgregarUser')
        self.btnEliminarUser = QPushButton('Eliminar', objectName = 'btnEliminarUser')
        self.btnModificarUser = QPushButton('Modificar', objectName = 'btnModificarUser')
        self.btnEjecutarAgregar = QPushButton('Ejecutar', objectName = 'btnEjecutarAgregar')
        self.btnEjecutarEliminar = QPushButton('Ejecutar', objectName = 'btnEjecutarEliminar')
        self.btnEjecutarModificar = QPushButton('Ejecutar', objectName = 'btnEjecutarModificar')
        self.btnAceptarModificar = QPushButton('Aceptar', objectName = 'btnAceptarModificar')
        self.btnIngresarAdminProd = QPushButton('Ingresa', objectName = 'btnIngresarAdminProd')
        self.btnAgregarProductos = QPushButton('Agregar', objectName = 'btnAgregarProductos')
        self.btnEliminarProductos = QPushButton('Eliminar', objectName = 'btnEliminarProductos')
        self.btnEjecutarAgregarP = QPushButton('Ejecutar', objectName = 'btnEjecutarAgregarP')
        self.btnEjecutarEliminarP = QPushButton('Ejecutar', objectName = 'btnEjecutarEliminarP')
        
        # Combo box
        self.btnTipoCafe = QComboBox(objectName = 'btnTipoCafe') # Menú desplegable "Tipo de Café"
        self.btnSabor = QComboBox(objectName = 'btnSabor') # Menú desplegable "Sabor"
        self.btnTamanio = QComboBox(objectName = 'btnTamanio') # Menú desplegable "Tamaño"
        self.btnTipoLeche = QComboBox(objectName = 'btnTipoLeche') # Menú desplegable "Tipo de Leche"
        self.btnExtras = QComboBox(objectName = 'btnExtras') # Menú desplegable "Extras"
        self.btnTipoPedido = QComboBox(objectName = 'btnTipoPedido') # Menú desplegable "Tipo de Pedido"
        self.comboCategoriaModificar = QComboBox(objectName = 'comboCategoriaModificar')
        self.comboOpcionesModificar = QComboBox(objectName = 'comboOpcionesModificar')
        self.comboUsuario = QComboBox(objectName = 'comboUsuario')
        self.comboIdProductos = QComboBox(objectName = 'comboIdProductos')

        # Campos de texto
        self.cNombreCliente = QLineEdit(objectName = 'cNombreCliente') # Campo de texto "Nombre del cliente"
        self.cT1 = QLineEdit(objectName = 'cT1')
        self.cT2 = QLineEdit(objectName = 'cT2')
        self.cT3 = QLineEdit(objectName = 'cT3')
        self.cT4 = QLineEdit(objectName = 'cT4')
        self.campoUsuario = QLineEdit(objectName = 'campoUsuario')
        self.campoContrasenia = QLineEdit(objectName = 'campoContrasenia')
        self.campoNombreAgregar = QLineEdit(objectName = 'campoNombreAgregar')
        self.campoUsuarioAgregar = QLineEdit(objectName = 'campoUsuarioAgregar')
        self.campoContraseniaAgregar = QLineEdit(objectName = 'campoContraseniaAgregar')
        self.campoTipoAgregar = QLineEdit(objectName = 'campoTipoAgregar')
        self.campoValorModificar = QLineEdit(objectName = 'campoValorModificar')
        self.campoUsuarioProductos = QLineEdit(objectName = 'campoUsuarioProductos')
        self.campoContraseniaProductos = QLineEdit(objectName = 'campoContraseniaProductos')
        self.campoIdProductos = QLineEdit(objectName = 'campoIdProductos')
        self.campoNombreProductos = QLineEdit(objectName = 'campoNombreProductos')

        self.cNombreCliente.setPlaceholderText('Nombre del cliente')
        self.campoUsuario.setPlaceholderText('Usuario')
        self.campoContrasenia.setPlaceholderText('Contraseña')
        self.campoNombreAgregar.setPlaceholderText('Nombre empleado')
        self.campoUsuarioAgregar.setPlaceholderText('Usuario')
        self.campoContraseniaAgregar.setPlaceholderText('Contraseña')
        self.campoTipoAgregar.setPlaceholderText('Privilegio')
        self.campoValorModificar.setPlaceholderText('Información a Modificar')
        self.campoUsuarioProductos.setPlaceholderText('Usuario')
        self.campoContraseniaProductos.setPlaceholderText('Contraseña')
        self.campoIdProductos.setPlaceholderText('ID')
        self.campoNombreProductos.setPlaceholderText('Nombre')
        
        #Etiquetas
        self.logoCafe = QLabel('') # Logo del Café
        self.pedidoLabel = QLabel('Pedidos')
        self.inventarioLabel = QLabel('Inventario')
        self.materiaPrimaLabel = QLabel('Administración de Materia Prima')
        self.adminUsuariosLabel = QLabel('Administración de Usuarios')
        self.adminProductosLabel = QLabel('Administración de Productos')
        self.autenticarUsuariosLabel = QLabel('')
        self.confirmacionUsuariosLabel = QLabel('')
        self.lAutenticarUsuariosP = QLabel('')
        self.lConfirmacionOperacionP = QLabel('')
        self.label2 = QLabel('')
        self.label3 = QLabel('')
        self.label4 = QLabel('')
        self.label5 = QLabel('')
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
        self.tablaAMateriaPrima = QTableWidget(4, 3)
        self.tablaUsuarios = QTableWidget(3, 2)
        self.tablaAdminProductos = QTableWidget(2, 2)

        self.tablaInventario.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablaVentasDia.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablaVentasMes.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablaAMateriaPrima.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablaUsuarios.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablaAdminProductos.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # ESTTILOS
        # Hojas de Estilos
        self.btnPedidos.setStyleSheet('border: none; color: white;')
        self.btnAdminMatP.setStyleSheet('border: none;\ncolor: white;')
        self.btnInventario.setStyleSheet('border: none; color: white;')
        self.btnVentas.setStyleSheet('border: none; color: white;')
        self.btnAdminUsuarios.setStyleSheet('border: none;\ncolor: white;')
        self.btnAdminProductos.setStyleSheet('border: none;\ncolor: white;')
        self.pedidoSS = """
                            QComboBox { 
                                        border-radius: 10px; 
                                        color: white;
                                        }

                            QLineEdit {
                                    border: 1px solid #d4c3b8;
                                    border-radius: 5px;
                                    background-color: #d4c3b8;
                                    color: black;
                                    }

                            QPushButton {
                                    border: 1px solid brown;
                                    border-radius: 5px;
                                    background-color: brown;
                                    color: white;
                            }
                            
                            QLabel {
                                font: 48pt \"Vladimir Script\";
                                color: #6b350a;
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
        self.inventarioLabel.setStyleSheet('font: 48pt \"Vladimir Script\";\ncolor: #6b350a;')
        self.materiaPrimaLabel.setStyleSheet('font: 48pt \"Vladimir Script\";\ncolor: #6b350a;')
        self.adminUsuariosLabel.setStyleSheet('font: 48pt \"Vladimir Script\";\ncolor: #6b350a;')
        self.adminProductosLabel.setStyleSheet('font: 48pt \"Vladimir Script\";\ncolor: #6b350a;')

        # Configuración de Fuentes de los Widgets
        self.btnPedidos.setFont(self.negrita14) # -> Inicia Conf. QPushButton
        self.btnInventario.setFont(self.negrita14)
        self.btnVentas.setFont(self.negrita14)
        self.btnAdminMatP.setFont(self.negrita14)
        self.btnAdminUsuarios.setFont(self.negrita14)
        self.btnAdminProductos.setFont(self.negrita14)
        self.btnFinalizarP.setFont(self.negrita14) 
        self.btnAgregarP.setFont(self.negrita14) # <- Termina Conf. QPushButton
        self.btnTipoCafe.setFont(self.negrita14) # -> Inicia Conf. QComboBox
        self.btnSabor.setFont(self.negrita14)
        self.btnTamanio.setFont(self.negrita14)
        self.btnTipoLeche.setFont(self.negrita14)
        self.btnExtras.setFont(self.negrita14)
        self.btnTipoPedido.setFont(self.negrita14)
        self.cNombreCliente.setFont(self.negrita14) # <- Termina Conf. QComboBox
        self.ventasDiaL.setFont(self.negrita14) # -> Inicia Conf. QLabel
        self.ventasMesL.setFont(self.negrita14) # -> Termina Conf. QLablel

        #Configuración de tamaño de los Widgets
        self.btnPedidos.setFixedSize(260, 50) # -> Inicia Conf. QPushButton
        self.btnInventario.setFixedSize(260, 50)
        self.btnVentas.setFixedSize(260, 50)
        self.btnAdminMatP.setFixedSize(260, 50)
        self.btnAdminUsuarios.setFixedSize(260, 50)
        self.btnAdminProductos.setFixedSize(260, 50)
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
        self.autenticarUsuariosLabel.setFixedHeight(50)
        self.lAutenticarUsuariosP.setFixedHeight(50)
        self.tablaInventario.setFixedSize(1260, 200) # <- Termina Conf. QLabel

        # Alineación
        self.inventarioLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ventasLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.materiaPrimaLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.adminProductosLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.adminUsuariosLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #Configuración de iconos
        self.btnPedidos.setIcon(QIcon('./Recursos/Iconos/tCafe.png'))
        self.btnInventario.setIcon(QIcon('./Recursos/Iconos/inventario.png'))
        self.btnVentas.setIcon(QIcon('./Recursos/Iconos/ventas.png'))
        self.btnAdminMatP.setIcon(QIcon('./Recursos/Iconos/materiaPrima.png'))
        self.btnAdminProductos.setIcon(QIcon('./Recursos/Iconos/productos.png'))
        self.btnAdminUsuarios.setIcon(QIcon('./Recursos/Iconos/usuario.png'))
        self.btnPedidos.setIconSize(QSize(35, 35))
        self.btnInventario.setIconSize(QSize(35, 35))
        self.btnVentas.setIconSize(QSize(35, 35))
        self.btnAdminMatP.setIconSize(QSize(35, 35))
        self.btnAdminProductos.setIconSize(QSize(35, 35))
        self.btnAdminUsuarios.setIconSize(QSize(35, 35))

        # Opciones para tablas
        self.tablaInventario.setHorizontalHeaderLabels(['ID', 'Nombre del producto', 'Categoría', 'Ubicación', 'Cantidad', 'Costo unitario'])
        self.tablaVentasDia.setHorizontalHeaderLabels(['Horas', 'Número de ventas'])
        self.tablaVentasMes.setHorizontalHeaderLabels(['Semana', 'Número de ventas'])
        self.tablaAdminProductos.setHorizontalHeaderLabels(['ID', 'Nombre'])
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
        self.btnAdminMatP.clicked.connect(self.botonAdminMatP)
        self.btnAdminUsuarios.clicked.connect(self.botonAdminUsuarios)
        self.btnAdminProductos.clicked.connect(self.botonAdminProductos)
        self.btnAgregar.clicked.connect(self.btn_Agregar)
        self.btnEliminar.clicked.connect(self.btn_Eliminar)

        # Pestañas
        self.tab1 = self.ventanaPedidos()
        self.tab2 = self.ventanaInventario()
        self.tab3 = self.ventanaVentas()
        self.tab4 = self.ventanaAdminMatP()
        self.tab5 = self.administracionUsuarios()
        self.tab6 = self.administracionProductos()

        self.principal() # Se llama a la pestaña principal
        self.showMaximized() # Despliega "maximizada la pantalla principal"

    def principal(self):
        left_layout = QVBoxLayout() # Layout Vertical
        left_layout.addWidget(self.logoCafe) # Imagen del logo del café
        left_layout.addSpacerItem(QSpacerItem(260, 15))
        left_layout.addWidget(self.btnPedidos) # Botón para página Pedidos
        left_layout.addWidget(self.btnInventario) # Botón para página inventario
        left_layout.addWidget(self.btnVentas) # Botón para página ventas
        left_layout.addWidget(self.btnAdminMatP)
        left_layout.addWidget(self.btnAdminUsuarios)
        left_layout.addWidget(self.btnAdminProductos)
        left_layout.addStretch(5) # Alineado desde bottom a top
        left_widget = QWidget() # Intancia de la clase QWidget
        left_widget.setStyleSheet('background-color: #6b350a;')
        left_widget.setFixedWidth(260)
        left_widget.setLayout(left_layout) # Se define el layout del documento

        self.right_widget = QTabWidget() 
        self.right_widget.tabBar().setObjectName("mainTab")

        self.right_widget.addTab(self.tab1, '')
        self.right_widget.addTab(self.tab2, '')
        self.right_widget.addTab(self.tab3, '')
        self.right_widget.addTab(self.tab4, '')
        self.right_widget.addTab(self.tab5, '')
        self.right_widget.addTab(self.tab6, '')

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
        self.btnPedidos.setStyleSheet('background-color: #896950; border: none; color: white;')
        self.btnInventario.setStyleSheet('background-color: #6b350a; border: none; color: white;')
        self.btnVentas.setStyleSheet('background-color: #6b350a; border: none; color: white;')
        self.btnAdminMatP.setStyleSheet('background-color: #6b350a; border: none; color: white;')
        self.btnAdminUsuarios.setStyleSheet('background-color: #6b350a; border: none; color: white;')
        self.btnAdminProductos.setStyleSheet('background-color: #6b350a; border: none; color: white;')

    def botonInventario(self):
        self.right_widget.setCurrentIndex(1)
        self.btnPedidos.setStyleSheet('background-color: #6b350a; border: none; color: white;')
        self.btnInventario.setStyleSheet('background-color: #896950; border: none; color: white;')
        self.btnVentas.setStyleSheet('background-color: #6b350a; border: none; color: white;')
        self.btnAdminMatP.setStyleSheet('background-color: #6b350a; border: none; color: white;')
        self.btnAdminUsuarios.setStyleSheet('background-color: #6b350a; border: none; color: white;')
        self.btnAdminProductos.setStyleSheet('background-color: #6b350a; border: none; color: white;')

    def botonVentas(self):
        self.right_widget.setCurrentIndex(2)
        self.btnPedidos.setStyleSheet('background-color: #6b350a; border: none; color: white;')
        self.btnInventario.setStyleSheet('background-color: #6b350a; border: none; color: white;')
        self.btnVentas.setStyleSheet('background-color: #896950; border: none; color: white;')
        self.btnAdminMatP.setStyleSheet('background-color: #6b350a; border: none; color: white;')
        self.btnAdminUsuarios.setStyleSheet('background-color: #6b350a; border: none; color: white;')
    
    def botonAdminMatP(self):
        self.right_widget.setCurrentIndex(3)
        self.btnPedidos.setStyleSheet('background-color: #6b350a; border: none; color: white;')
        self.btnInventario.setStyleSheet('background-color: #6b350a; border: none; color: white;')
        self.btnVentas.setStyleSheet('background-color: #6b350a; border: none; color: white;')
        self.btnAdminMatP.setStyleSheet('background-color: #896950; border: none; color: white;')
        self.btnAdminUsuarios.setStyleSheet('background-color: #6b350a; border: none; color: white;')
        self.btnAdminProductos.setStyleSheet('background-color: #6b350a; border: none; color: white;')

    def botonAdminUsuarios(self):
        self.right_widget.setCurrentIndex(4)
        self.btnPedidos.setStyleSheet('background-color: #6b350a; border: none; color: white;')
        self.btnInventario.setStyleSheet('background-color: #6b350a; border: none; color: white;')
        self.btnVentas.setStyleSheet('background-color: #6b350a; border: none; color: white;')
        self.btnAdminMatP.setStyleSheet('background-color: #6b350a; border: none; color: white;')
        self.btnAdminUsuarios.setStyleSheet('background-color: #896950; border: none; color: white;')
        self.btnAdminProductos.setStyleSheet('background-color: #6b350a; border: none; color: white;')

    def botonAdminProductos(self):
        self.right_widget.setCurrentIndex(5)
        self.btnPedidos.setStyleSheet('background-color: #6b350a; border: none; color: white;')
        self.btnInventario.setStyleSheet('background-color: #6b350a; border: none; color: white;')
        self.btnVentas.setStyleSheet('background-color: #6b350a; border: none; color: white;')
        self.btnAdminMatP.setStyleSheet('background-color: #6b350a; border: none; color: white;')
        self.btnAdminUsuarios.setStyleSheet('background-color: #6b350a; border: none; color: white;')
        self.btnAdminProductos.setStyleSheet('background-color: #896950; border: none; color: white;')
    
    def btn_Agregar(self):
        self.label2.setText('ID')
        self.label3.setText('Nombre')
        self.label4.setText('Categoría')

        self.label2.setFont(self.negrita14)
        self.label3.setFont(self.negrita14)
        self.label4.setFont(self.negrita14)

        self.cT1.setEnabled(True)
        self.cT2.setEnabled(True)
        self.cT3.setEnabled(True)

        self.cT1.setStyleSheet('border: 1px solid black;\nborder-radius: 5px;')
        self.cT2.setStyleSheet('border: 1px solid black;\nborder-radius: 5px;')
        self.cT3.setStyleSheet('border: 1px solid black;\nborder-radius: 5px;')

        self.cT1.setFont(self.negrita14)
        self.cT2.setFont(self.negrita14)
        self.cT3.setFont(self.negrita14)

        self.btnAceptar1.setStyleSheet('border: 1px solid brown;\nborder-radius: 5px;\nbackground-color: brown;\ncolor: white;')
        self.btnAceptar1.setEnabled(True)
        
    def btn_Eliminar(self):
        self.label5.setText('ID')
        self.label5.setFont(self.negrita14)

        self.cT4.setEnabled(True)
        self.cT4.setStyleSheet('border: 1px solid black; border-radius: 5px;')
        self.cT4.setFont(self.negrita14)

        self.btnAceptar2.setStyleSheet('border: 1px solid brown;\nborder-radius: 5px;\nbackground-color: brown;\ncolor: white;')
        self.btnAceptar2.setEnabled(True)
	
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

    def ventanaAdminMatP(self):
        self.materiaPrimaLabel.setText('Administración de Materia Prima')

        self.cT1.setStyleSheet("border: none;\nbackground-color: white;")
        self.cT2.setStyleSheet("border: none;\nbackground-color: white;")
        self.cT3.setStyleSheet("border: none;\nbackground-color: white;")
        self.cT4.setStyleSheet("border: none;\nbackground-color: white;")

        self.cT1.setEnabled(False)
        self.cT2.setEnabled(False)
        self.cT3.setEnabled(False)
        self.cT4.setEnabled(False)

        self.btnAgregar.setStyleSheet('border: 1px solid green;\nborder-radius: 5px;\nbackground-color: green;\ncolor: white;')
        self.btnEliminar.setStyleSheet('border: 1px solid red;\nborder-radius: 5px;\nbackground-color: red;\ncolor: white;')
        self.btnAceptar1.setStyleSheet('border: 1px solid white;\nborder-radius: 5px;\nbackground-color: white;\ncolor: white;')
        self.btnAceptar2.setStyleSheet('border: 1px solid white;\nborder-radius: 5px;\nbackground-color: white;\ncolor: white;')

        self.btnAgregar.setFont(self.negrita14)
        self.btnEliminar.setFont(self.negrita14)
        self.btnAceptar1.setFont(self.negrita14)
        self.btnAceptar2. setFont(self.negrita14)

        self.btnAceptar1.setEnabled(False)
        self.btnAceptar2.setEnabled(False)
        
        self.tablaAMateriaPrima.setHorizontalHeaderLabels(['ID', 'Nombre', 'Categoría'])
        self.tablaAMateriaPrima.resizeRowsToContents()
        self.tablaAMateriaPrima.resizeColumnsToContents()
        self.tablaAMateriaPrima.setStyleSheet('border: none;')
        
        vbox = QVBoxLayout()
        vbox1 = QVBoxLayout()
        main_layout = QVBoxLayout()
        hbox = QHBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()

        hbox.addWidget(self.label2)
        hbox.addWidget(self.label3)
        hbox.addWidget(self.label4)

        hbox1.addWidget(self.cT1)
        hbox1.addWidget(self.cT2)
        hbox1.addWidget(self.cT3)

        vbox.addWidget(self.btnAgregar)
        vbox.addLayout(hbox)
        vbox.addLayout(hbox1)
        vbox.addWidget(self.btnAceptar1)

        vbox1.addWidget(self.btnEliminar)
        vbox1.addWidget(self.label5)
        vbox1.addWidget(self.cT4)
        vbox1.addWidget(self.btnAceptar2)
        
        hbox2.addLayout(vbox)
        hbox2.addLayout(vbox1)

        main_layout.addWidget(self.materiaPrimaLabel)
        main_layout.addWidget(self.tablaAMateriaPrima, Qt.AlignmentFlag.AlignVCenter)
        main_layout.addLayout(hbox2)
        
        main = QWidget()
        main.setLayout(main_layout)
        return main

    def administracionUsuarios(self):
        self.autenticarUsuariosLabel.setStyleSheet('background-color: black;')
        main_layout = QVBoxLayout()
        vbox = QVBoxLayout()
        vbox1 = QVBoxLayout()
        vbox2 = QVBoxLayout()
        vbox3 = QVBoxLayout()
        hbox = QHBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()

        vbox.addWidget(self.autenticarUsuariosLabel)
        vbox.addWidget(self.campoUsuario)
        vbox.addWidget(self.campoContrasenia)
        vbox.addWidget(self.btnIngresar)

        hbox.addWidget(self.tablaUsuarios)
        hbox.addLayout(vbox)

        vbox1.addWidget(self.btnAgregarUser)
        vbox1.addWidget(self.campoNombreAgregar)
        vbox1.addWidget(self.campoUsuarioAgregar)
        vbox1.addWidget(self.campoContraseniaAgregar)
        vbox1.addWidget(self.campoTipoAgregar)
        vbox1.addWidget(self.btnEjecutarAgregar)

        vbox2.addWidget(self.btnEliminarUser)
        vbox2.addWidget(self.comboUsuario)
        vbox2.addWidget(self.btnEjecutarEliminar)

        hbox1.addWidget(self.comboCategoriaModificar)
        hbox1.addWidget(self.btnAceptarModificar)

        vbox3.addWidget(self.btnModificarUser)
        vbox3.addLayout(hbox1)
        vbox3.addWidget(self.comboOpcionesModificar)
        vbox3.addWidget(self.campoValorModificar)
        vbox3.addWidget(self.btnEjecutarModificar)

        hbox2.addLayout(vbox1)
        hbox2.addLayout(vbox2)
        hbox2.addLayout(vbox3)

        main_layout.addWidget(self.adminUsuariosLabel)
        main_layout.addLayout(hbox)
        main_layout.addLayout(hbox2)
        main_layout.addWidget(self.confirmacionUsuariosLabel)
        main = QWidget()
        main.setLayout(main_layout)
        return main

    def administracionProductos(self):
        main_layout = QVBoxLayout()
        vbox = QVBoxLayout()
        vbox1 = QVBoxLayout()
        vbox2 = QVBoxLayout()
        hbox = QHBoxLayout()
        hbox1 = QHBoxLayout()

        vbox.addWidget(self.lAutenticarUsuariosP)
        vbox.addWidget(self.campoUsuarioProductos)
        vbox.addWidget(self.campoContraseniaProductos)
        vbox.addWidget(self.btnIngresarAdminProd)

        hbox.addWidget(self.tablaAdminProductos)
        hbox.addLayout(vbox)

        vbox1.addWidget(self.btnAgregarProductos)
        vbox1.addWidget(self.campoIdProductos)
        vbox1.addWidget(self.campoNombreProductos)
        vbox1.addWidget(self.btnEjecutarAgregarP)

        vbox2.addWidget(self.btnEliminarProductos)
        vbox2.addWidget(self.comboIdProductos)
        vbox2.addWidget(self.btnEjecutarEliminarP)

        hbox1.addLayout(vbox1)
        hbox1.addLayout(vbox2)

        main_layout.addWidget(self.adminProductosLabel)
        main_layout.addLayout(hbox)
        main_layout.addLayout(hbox1)
        main_layout.addWidget(self.lConfirmacionOperacionP)
        main = QWidget()
        main.setLayout(main_layout)
        return main


if __name__ == '__main__':
    app = QApplication(sys.argv)
    #window = Window()
    Login = QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec())
