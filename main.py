from PyQt6.QtCore import *
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import *
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # set the title of main window
        self.setWindowTitle('Cafeteria')
        self.setStyleSheet('background-color: white;')

        # set the size of window
        self.Width = 800
        self.height = int(0.618 * self.Width)
        self.resize(self.Width, self.height)
		
		# add all widgets
        self.btn_1 = QPushButton('Pedido', self)
        self.btn_2 = QPushButton('Inventario', self)
        self.btn_3 = QPushButton('Ventas', self)
        self.logoCafe = QLabel('')
        self.pixmapCafe = QPixmap('./Recursos/Imagenes/logoCafe.png')
        self.pixmapCafe.scaled(60, 60)
        self.logoCafe.setPixmap(self.pixmapCafe)

        # Hoja de estilos
        self.btn_1.setStyleSheet('border: none;')
        self.btn_2.setStyleSheet('border: none;')
        self.btn_3.setStyleSheet('border: none;')


        self.btn_1.clicked.connect(self.button1)
        self.btn_2.clicked.connect(self.button2)
        self.btn_3.clicked.connect(self.button3)

        # add tabs
        self.tab1 = self.ui1()
        self.tab2 = self.ui2()
        self.tab3 = self.ui3()

        self.initUI()
        self.showMaximized()

    def initUI(self):
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.logoCafe)
        left_layout.addWidget(self.btn_1)
        left_layout.addWidget(self.btn_2)
        left_layout.addWidget(self.btn_3)
        left_layout.addStretch(5)
        left_layout.setSpacing(20)
        left_widget = QWidget()
        left_widget.setStyleSheet("background-color: brown;")
        left_widget.setLayout(left_layout)

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
        main_layout.addWidget(QLabel('Pedidos'))
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main

    def ui2(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('Inventario'))
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
    ex = Window()
    ex.show()
    sys.exit(app.exec())