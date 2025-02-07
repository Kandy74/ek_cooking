from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView, QHeaderView

from dao.type_father import add_type_father, type_father_exist, get_all_type_father
from entity.type_father_model import FatherType


class Ui_Form(QWidget):
    def __init__(self):
        super(Ui_Form, self).__init__()
        self.setupUi(self)
        self.show_type()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(453, 534)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../img/新增.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form.setWindowIcon(icon)
        self.groupBox = QtWidgets.QGroupBox(parent=Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 70, 411, 201))
        self.groupBox.setObjectName("groupBox")
        self.line_type_id = QtWidgets.QLineEdit(parent=self.groupBox)
        self.line_type_id.setGeometry(QtCore.QRect(110, 30, 281, 21))
        self.line_type_id.setObjectName("line_type_id")
        self.line_type_name = QtWidgets.QLineEdit(parent=self.groupBox)
        self.line_type_name.setGeometry(QtCore.QRect(110, 70, 281, 21))
        self.line_type_name.setObjectName("line_type_name")
        self.plain_decs = QtWidgets.QPlainTextEdit(parent=self.groupBox)
        self.plain_decs.setGeometry(QtCore.QRect(20, 100, 371, 81))
        self.plain_decs.setObjectName("plain_decs")
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
        self.pb_add = QtWidgets.QPushButton(parent=Form)
        self.pb_add.setGeometry(QtCore.QRect(80, 500, 75, 23))
        # 绑定按钮点击事件
        self.pb_add.clicked.connect(self.add_type)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../geological_supervision_system/img/新增.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        self.pb_add.setIcon(icon1)
        self.pb_add.setObjectName("pb_add")
        self.pb_reset = QtWidgets.QPushButton(parent=Form)
        self.pb_reset.setGeometry(QtCore.QRect(300, 500, 75, 23))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../geological_supervision_system/img/reset_ico.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        self.pb_reset.setIcon(icon2)
        self.pb_reset.setObjectName("pb_reset")
        # 绑定按钮点击事件
        self.pb_reset.clicked.connect(self.reset)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=Form)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 280, 411, 211))
        self.groupBox_2.setObjectName("groupBox_2")
        self.tab_type = QtWidgets.QTableWidget(parent=self.groupBox_2)
        self.tab_type.setGeometry(QtCore.QRect(10, 20, 391, 181))
        self.tab_type.setObjectName("tab_type")
        self.tab_type.setColumnCount(0)
        self.tab_type.setRowCount(0)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "产品类别添加系统"))
        self.groupBox.setTitle(_translate("Form", "类别添加"))
        self.line_type_id.setPlaceholderText(_translate("Form", "格式：0000,00（占位）00（序号）"))
        self.line_type_name.setPlaceholderText(_translate("Form", "填写类别名称"))
        self.plain_decs.setPlaceholderText(_translate("Form", "备注说明："))
        self.label.setText(_translate("Form", "类别代码："))
        self.label_2.setText(_translate("Form", "类别名称："))
        self.label_3.setText(_translate("Form", "EK烘焙 产品类别添加系统"))
        self.pb_add.setText(_translate("Form", "添加"))
        self.pb_reset.setText(_translate("Form", "重置"))
        self.groupBox_2.setTitle(_translate("Form", "类别列表"))

    def add_type(self):
        """
        使用add_type_father方法添加类别信息
        :return:
        """
        # 调取输入框中类别的代码
        type_id = self.line_type_id.text()
        # 调取输入框中类别的名称
        type_name = self.line_type_name.text()
        # 调取输入框中类别的描述
        decs = self.plain_decs.toPlainText()
        if type_id == "" or type_name == "":
            QtWidgets.QMessageBox.warning(self, "警告", "类别代码或名称不能为空！")
        elif type_father_exist(type_id, type_name):
            QtWidgets.QMessageBox.warning(self, "警告", "该类别已存在！请检查类别代码和名称！")
        else:
            new_type = FatherType(type_id, type_name, decs)
            if add_type_father(new_type):
                QtWidgets.QMessageBox.information(self, "提示", "添加成功！")
        self.show_type()

    def reset(self):
        """
        重置输入框内容
        :return:
        """
        self.line_type_id.clear()
        self.line_type_name.clear()
        self.plain_decs.clear()

    def show_type(self):
        """
        显示类别列表
        :return:
        """
        # 通过dao方法，传入table列表变量里
        table =  get_all_type_father()

        row = 0
        if table:
            row = len(table)
        #  设置行和列，这两个必须设置 不然不显示，而且要往前放
        self.tab_type.setRowCount(row)
        self.tab_type.setColumnCount(3)

        for i in range(row):
            for j in range(3):
                data = QTableWidgetItem(str(table[i][j]))
                self.tab_type.setItem(i, j, data)
        # 隐藏垂直序号，即index
        self.tab_type.verticalHeader().setVisible(False)
        # 禁止编辑单元格
        self.tab_type.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        # 设置选择行为为按照行来选择
        self.tab_type.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        # 数据列宽自动匹配表格宽度
        self.tab_type.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        # 设置表头
        self.tab_type.setHorizontalHeaderLabels(['产品类别代码', '产品类别名称', '备注'])

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Form()
    ui.show()
    sys.exit(app.exec())
