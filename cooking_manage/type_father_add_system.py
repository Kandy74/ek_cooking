import sys

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget, QApplication


class Ui_Form(QWidget):
    def __init__(self):
        super(Ui_Form, self).__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(453, 534)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../img/新增.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form.setWindowIcon(icon)
        self.groupBox = QtWidgets.QGroupBox(parent=Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 70, 411, 201))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(110, 30, 281, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 70, 281, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(parent=self.groupBox)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 100, 371, 81))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 30, 53, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 53, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(60, 20, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(80, 500, 75, 23))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../geological_supervision_system/img/新增.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 500, 75, 23))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../geological_supervision_system/img/reset_ico.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=Form)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 280, 411, 211))
        self.groupBox_2.setObjectName("groupBox_2")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.groupBox_2)
        self.tableWidget.setGeometry(QtCore.QRect(10, 20, 391, 181))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "产品大类添加系统"))
        self.groupBox.setTitle(_translate("Form", "大类添加"))
        self.lineEdit.setPlaceholderText(_translate("Form", "格式：0000,00（占位）00（序号）"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "填写大类名称"))
        self.plainTextEdit.setPlaceholderText(_translate("Form", "备注说明："))
        self.label.setText(_translate("Form", "大类代码："))
        self.label_2.setText(_translate("Form", "大类名称："))
        self.label_3.setText(_translate("Form", "EK烘焙 产品大类添加系统"))
        self.pushButton.setText(_translate("Form", "添加"))
        self.pushButton_2.setText(_translate("Form", "重置"))
        self.groupBox_2.setTitle(_translate("Form", "大类列表"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Ui_Form()
    ui.show()
    sys.exit(app.exec())
