import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "prueba.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btn.clicked.connect(self.calculos)

    def calculos(self):
        precio = int(self.txt_cantidad.toPlainText())
        desc = (self.spin_descuento.value())
        total  =  ((desc/100)*precio)
        total_st = "su pago es de :" + str(total)
        self.txt_resultado.setText(total_st)

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())