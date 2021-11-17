from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
import sys

class Ventana(QWidget):
    def __init__(self):
        super().__init__() 
        self.setWindowTitle('Cafeteria')
        self.showMaximized()
        
        boton1 = QPushButton('Finalizar Pedido')
        boton1.setFixedSize(70, 50)

        grid = QGridLayout()
        grid.addWidget(boton1, 10, 10)
        self.setLayout(grid)


app = QApplication(sys.argv)

ventana = Ventana()
ventana.show()

sys.exit(app.exec())