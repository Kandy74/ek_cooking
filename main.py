import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow, QApplication

from product import product_add_system, product_manage_system
from type_father import type_father_add_system, type_father_manage_system


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.type_father_add_system = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/LOGOdangao.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # 设置背景图片
        self.centralwidget.setStyleSheet("background-image: url(img/系统操作界面1.jpg);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 22))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(parent=self.menubar)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.menu.setFont(font)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(parent=self.menu)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.menu_2.setFont(font)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(parent=self.menu)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.menu_3.setFont(font)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(parent=self.menubar)
        self.menu_4.setObjectName("menu_4")
        self.menu_5 = QtWidgets.QMenu(parent=self.menubar)
        self.menu_5.setObjectName("menu_5")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.action_3 = QtGui.QAction(parent=MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/新增.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.action_3.setIcon(icon1)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtGui.QAction(parent=MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/整改通知.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.action_4.setIcon(icon2)
        self.action_4.setObjectName("action_4")
        # 打开产品类别管理窗口
        self.action_4.triggered.connect(self.open_type_father_manage_system)
        self.action_6 = QtGui.QAction(parent=MainWindow)
        self.action_6.setIcon(icon1)
        self.action_6.setObjectName("action_6")
        # 打开产品添加窗口
        self.action_6.triggered.connect(self.open_product_add_system)
        self.action_7 = QtGui.QAction(parent=MainWindow)
        self.action_7.setIcon(icon2)
        self.action_7.setObjectName("action_7")
        # 打开产品管理窗口
        self.action_7.triggered.connect(self.open_product_manage_system)
        self.menu_2.addAction(self.action_3)
        self.menu_2.addAction(self.action_4)

        self.menu_3.addSeparator()
        self.menu_3.addAction(self.action_6)
        self.menu_3.addAction(self.action_7)
        self.menu.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
        # 点击action_3打开type_father_add_system窗口

        self.action_3.triggered.connect(self.open_type_father_add_system)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EK烘焙集成管理平台"))
        self.menu.setTitle(_translate("MainWindow", "数据库管理"))
        self.menu_2.setTitle(_translate("MainWindow", "产品类别管理"))
        self.menu_3.setTitle(_translate("MainWindow", "产品管理"))
        self.menu_4.setTitle(_translate("MainWindow", "盘点系统"))
        self.menu_5.setTitle(_translate("MainWindow", "配料表管理系统"))
        self.action_3.setText(_translate("MainWindow", "添加产品类别"))
        self.action_4.setText(_translate("MainWindow", "产品类别信息维护"))
        self.action_6.setText(_translate("MainWindow", "添加产品"))
        self.action_7.setText(_translate("MainWindow", "产品类别信息维护"))

    def open_type_father_add_system(self):
        """
        打开产品类别添加窗口
        :return:
        """
        self.type_father_add_system = type_father_add_system.Ui_Form()
        self.type_father_add_system.show()

    def open_type_father_manage_system(self):
        """
        打开产品类别管理窗口
        :return:
        """
        self.type_father_manage_system = type_father_manage_system.Ui_Form()
        self.type_father_manage_system.show()

    def open_product_add_system(self):
        """
        打开产品添加窗口
        :return:
        """
        self.product_add_system = product_add_system.Ui_Form()
        self.product_add_system.show()

    def open_product_manage_system(self):
        """
        打开产品管理窗口
        :return:
        """
        self.product_manage_system = product_manage_system.Ui_Form()
        self.product_manage_system.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()
    sys.exit(app.exec())
