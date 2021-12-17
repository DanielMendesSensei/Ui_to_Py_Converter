############## Ui to Py Converter ##############
############ Author: Daniel Mendes #############
################# Core Section #################
################# Version: 1.0 #################

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox, QAction
from PyQt5.QtGui import QPixmap, QIcon
import sys
import main_window
import os
import webbrowser

Logo = 'Logo.png'
class Ui_to_Py(QtWidgets.QMainWindow, main_window.Ui_Ui_to_Py):
    def __init__(self, parent=None):
        super(Ui_to_Py, self).__init__(parent)
        self.setupUi(self)
        self.actions()

    def actions(self):
        self.pushButton_1.clicked.connect(self.browse_file) 
        self.pushButton_2.clicked.connect(self.browse_folder)
        self.pushButton_3.clicked.connect(self.conversor)
        self.actionDoe.triggered.connect(self.doe)
        self.actionSobre_Ui_to_Py_Converter.triggered.connect(self.sobre)
    
    def browse_file(self):
        self.file_name, _ = QFileDialog.getOpenFileName(self,"Escolha o arquivo", "","QtDesinerUi Files (*.ui)")
        if self.file_name:
            self.path_1 = self.lineEdit.setText(self.file_name)

    def browse_folder(self):
        self.folder_name = QFileDialog.getExistingDirectory(self, "Selecione a pasta")
        self.path_2 = self.lineEdit_2.setText(self.folder_name)

    def conversor(self):
        c_1, c_2 = 'pyuic5', '-o'
        name_1 = '/teste.py'
        try:
            if self.path_1 == None and self.path_2 == None:
                comma = f'{c_1} "{self.file_name}" {c_2} "{self.folder_name}{name_1}"'
                os.system(comma)
                self.popup_concluido()

        except:
            self.popup_erro()

    def doe(self):
        mensagem = QMessageBox()
        mensagem.setWindowTitle("Doe! Ajude um Dev")
        mensagem.setText("Ajude com qualquer contribuição,\nLeia o QR Code!")
        mensagem.setWindowIcon(QtGui.QIcon(Logo))
        mensagem.setIconPixmap(QPixmap('Qr_Code.png'))
       
        sair = mensagem.exec_()

    def sobre(self):
        image = QIcon(Logo)
        mensagem = QMessageBox()
        mensagem.setWindowTitle("Sobre")
        mensagem.setWindowIcon(QtGui.QIcon(Logo))
        mensagem.setIconPixmap(image.pixmap(300, 300))
        mensagem.setText("Ui to Py Converter\nVersion: 1.0\nAuthor: Daniel Mendes\nGitHub: DanielMendesSeinsei")

        sair = mensagem.exec_()

    def popup_erro(self):
        mensagem = QMessageBox()
        mensagem.setWindowTitle("Erro!")
        mensagem.setText("Favor, insira o arquivo de entreda e a pasta de saída")
        mensagem.setWindowIcon(QtGui.QIcon(Logo))

        sair = mensagem.exec_()

    def popup_concluido(self):
        mensagem = QMessageBox()
        mensagem.setWindowTitle("Concluído!")
        mensagem.setText(f"Conversão feita com sucesso, salvo em: {self.folder_name}")
        mensagem.setWindowIcon(QtGui.QIcon(Logo))
        self.lineEdit.clear()
        self.lineEdit_2.clear() 

        sair = mensagem.exec_()


def main():
    app = QApplication(sys.argv)
    form = Ui_to_Py()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()