############## Ui to Py Converter ##############
############ Author: Daniel Mendes #############
################## UI Section ##################
################# Version: 1.0 #################

# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Ui_to_Py(object):
    def setupUi(self, Ui_to_Py):
        Ui_to_Py.setObjectName("Ui_to_Py")
        Ui_to_Py.resize(450, 250)
        Ui_to_Py.setMaximumSize(QtCore.QSize(450, 250))
        self.setWindowIcon(QtGui.QIcon('Logo.png'))
        self.centralwidget = QtWidgets.QWidget(Ui_to_Py)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_1 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_1.setGeometry(QtCore.QRect(10, 10, 261, 55))
        self.groupBox_1.setStyleSheet("")
        self.groupBox_1.setObjectName("groupBox_1")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_1)
        self.lineEdit.setGeometry(QtCore.QRect(10, 22, 241, 20))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 80, 261, 55))
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 20, 241, 20))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 100, 130, 25))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(300, 30, 130, 25))
        self.pushButton_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 170, 150, 30))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setObjectName("pushButton_3")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 450, 250))
        self.background.setStyleSheet("background-color:#F9F9F9")
        self.background.setText("")
        self.background.setObjectName("background")
        self.background.raise_()
        self.groupBox_1.raise_()
        self.groupBox_2.raise_()
        self.pushButton_2.raise_()
        self.pushButton_1.raise_()
        self.pushButton_3.raise_()
        Ui_to_Py.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Ui_to_Py)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 21))
        self.menubar.setObjectName("menubar")
        self.menuContribua = QtWidgets.QMenu(self.menubar)
        self.menuContribua.setObjectName("menuContribua")
        self.menuAjuda = QtWidgets.QMenu(self.menubar)
        self.menuAjuda.setObjectName("menuAjuda")
        Ui_to_Py.setMenuBar(self.menubar)
        self.actionDoe = QtWidgets.QAction(Ui_to_Py)
        self.actionDoe.setObjectName("actionDoe")
        self.actionSobre_Ui_to_Py_Converter = QtWidgets.QAction(Ui_to_Py)
        self.actionSobre_Ui_to_Py_Converter.setObjectName("actionSobre_Ui_to_Py_Converter")
        self.menuContribua.addAction(self.actionDoe)
        self.menuAjuda.addAction(self.actionSobre_Ui_to_Py_Converter)
        self.menubar.addAction(self.menuContribua.menuAction())
        self.menubar.addAction(self.menuAjuda.menuAction())

        self.retranslateUi(Ui_to_Py)
        QtCore.QMetaObject.connectSlotsByName(Ui_to_Py)
        

    def retranslateUi(self, Ui_to_Py):
        _translate = QtCore.QCoreApplication.translate
        Ui_to_Py.setWindowTitle(_translate("Ui_to_Py", "Ui to Py Converter"))
        self.groupBox_1.setTitle(_translate("Ui_to_Py", "Local Do Arquivo De Origem"))
        self.lineEdit.setPlaceholderText(_translate("Ui_to_Py", "Digite o caminho do arquivo de extensão .ui"))
        self.groupBox_2.setTitle(_translate("Ui_to_Py", "Local De Salvamento"))
        self.lineEdit_2.setPlaceholderText(_translate("Ui_to_Py", "Digite o caminho onde irá salvar o arquivo .py"))
        self.pushButton_2.setText(_translate("Ui_to_Py", "Procurar..."))
        self.pushButton_1.setText(_translate("Ui_to_Py", "Procurar..."))
        self.pushButton_3.setText(_translate("Ui_to_Py", "Converter!"))
        self.menuContribua.setTitle(_translate("Ui_to_Py", "Contribua"))
        self.menuAjuda.setTitle(_translate("Ui_to_Py", "Ajuda?"))
        self.actionDoe.setText(_translate("Ui_to_Py", "Doe!"))
        self.actionSobre_Ui_to_Py_Converter.setText(_translate("Ui_to_Py", "Sobre"))
