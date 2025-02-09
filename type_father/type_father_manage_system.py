import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView, QHeaderView

from dao.type_father import search_type_father, delete_type_father, update_type_father, type_father_exist
from entity.type_father_model import FatherType


class Ui_Form(QWidget):
    def __init__(self):
        super(Ui_Form, self).__init__()
        self.setupUi(self)
        self.search_type()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(702, 688)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../img/整改通知.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form.setWindowIcon(icon)
        self.groupBox = QtWidgets.QGroupBox(parent=Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 70, 661, 61))
        self.groupBox.setObjectName("groupBox")
        self.s_type_id = QtWidgets.QLineEdit(parent=self.groupBox)
        self.s_type_id.setGeometry(QtCore.QRect(120, 30, 131, 21))
        self.s_type_id.setObjectName("s_type_id")
        self.s_type_name = QtWidgets.QLineEdit(parent=self.groupBox)
        self.s_type_name.setGeometry(QtCore.QRect(370, 30, 161, 21))
        self.s_type_name.setObjectName("s_type_name")
        self.pb_search = QtWidgets.QPushButton(parent=self.groupBox)
        self.pb_search.setGeometry(QtCore.QRect(560, 30, 75, 23))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../img/search.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pb_search.setIcon(icon1)
        self.pb_search.setObjectName("pb_search")
        # 绑定槽函数，搜索按钮点击事件
        self.pb_search.clicked.connect(self.search_type)
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 81, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(280, 30, 81, 16))
        self.label_2.setObjectName("label_2")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=Form)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 150, 661, 291))
        self.groupBox_2.setObjectName("groupBox_2")
        self.tab_type_info = QtWidgets.QTableWidget(parent=self.groupBox_2)
        self.tab_type_info.setGeometry(QtCore.QRect(10, 20, 641, 261))
        self.tab_type_info.setObjectName("tab_type_info")
        self.tab_type_info.setColumnCount(0)
        self.tab_type_info.setRowCount(0)
        # 点击列表行触发槽函数，获取类别信息
        self.tab_type_info.clicked.connect(self.type_form)
        self.groupBox_3 = QtWidgets.QGroupBox(parent=Form)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 460, 661, 211))
        self.groupBox_3.setObjectName("groupBox_3")
        self.edit_type_id = QtWidgets.QLineEdit(parent=self.groupBox_3)
        self.edit_type_id.setGeometry(QtCore.QRect(110, 30, 181, 21))
        self.edit_type_id.setObjectName("edit_type_id")
        # 把edit_type_id设定为只读
        self.edit_type_id.setReadOnly(True)
        # 把edit_type_id设定浅灰色
        self.edit_type_id.setStyleSheet("background-color:lightgray;")
        self.edit_type_name = QtWidgets.QLineEdit(parent=self.groupBox_3)
        self.edit_type_name.setGeometry(QtCore.QRect(470, 30, 181, 21))
        self.edit_type_name.setObjectName("edit_type_name")
        self.edeit_desc = QtWidgets.QPlainTextEdit(parent=self.groupBox_3)
        self.edeit_desc.setGeometry(QtCore.QRect(10, 80, 641, 91))
        self.edeit_desc.setObjectName("edeit_desc")
        self.pb_modify = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pb_modify.setGeometry(QtCore.QRect(70, 180, 75, 23))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../img/modify.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pb_modify.setIcon(icon2)
        self.pb_modify.setObjectName("pb_modify")
        # 绑定槽函数，修改按钮点击事件
        self.pb_modify.clicked.connect(self.update_type)
        self.pb_reset = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pb_reset.setGeometry(QtCore.QRect(310, 180, 75, 23))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../img/reset_ico.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pb_reset.setIcon(icon3)
        self.pb_reset.setObjectName("pb_reset")
        # 绑定槽函数，重置按钮点击事件
        self.pb_reset.clicked.connect(self.reset_form)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButton_3.setGeometry(QtCore.QRect(520, 180, 75, 23))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../img/delete.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_3.setIcon(icon4)
        self.pushButton_3.setObjectName("pushButton_3")
        # 绑定槽函数，修改按钮点击事件,删除信息
        self.pushButton_3.clicked.connect(self.delete_type)
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(360, 30, 81, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(10, 60, 53, 15))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=Form)
        self.label_6.setGeometry(QtCore.QRect(160, 10, 441, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "产品类别信息维护系统"))
        self.groupBox.setTitle(_translate("Form", "产品类别搜索"))
        self.pb_search.setText(_translate("Form", "搜索"))
        self.label.setText(_translate("Form", "产品类别代码："))
        self.label_2.setText(_translate("Form", "产品类别名称："))
        self.groupBox_2.setTitle(_translate("Form", "产品类别列表"))
        self.groupBox_3.setTitle(_translate("Form", "产品类别信息维护"))
        self.pb_modify.setText(_translate("Form", "修改"))
        self.pb_reset.setText(_translate("Form", "重置"))
        self.pushButton_3.setText(_translate("Form", "删除"))
        self.label_3.setText(_translate("Form", "产品类别代码:"))
        self.label_4.setText(_translate("Form", "产品类别名称："))
        self.label_5.setText(_translate("Form", "备注说明："))
        self.label_6.setText(_translate("Form", "EK烘焙 产品类别信息维护系统"))

    def search_type(self):
        type_id = self.s_type_id.text()
        type_name = self.s_type_name.text()
        search_result = search_type_father(type_id=type_id, type_name=type_name)
        row = 0
        if search_result:
            row = len(search_result)
            #  设置行和列，这两个必须设置 不然不显示，而且要往前放
            self.tab_type_info.setRowCount(row)
            self.tab_type_info.setColumnCount(3)

            for i in range(row):
                for j in range(3):
                    data = QTableWidgetItem(str(search_result[i][j]))
                    self.tab_type_info.setItem(i, j, data)
            # 隐藏垂直序号，即index
            self.tab_type_info.verticalHeader().setVisible(False)
            # 禁止编辑单元格
            self.tab_type_info.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
            # 设置选择行为为按照行来选择
            self.tab_type_info.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
            # 数据列宽自动匹配表格宽度
            self.tab_type_info.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
            # 设置表头
            self.tab_type_info.setHorizontalHeaderLabels(['产品类别代码', '产品类别名称', '备注'])
        else:
            QtWidgets.QMessageBox.warning(self, "警告", "未查询到相关类别信息！")

    def delete_type(self):
        """
        删除类别信息
        :return:
        """
        replay = QtWidgets.QMessageBox.question(self, "提示", "确认删除该类别信息吗？",
                                                QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No,
                                                QtWidgets.QMessageBox.StandardButton.No)
        if replay == QtWidgets.QMessageBox.StandardButton.Yes:
            type_id = self.edit_type_id.text()
            if type_id:
                if delete_type_father(type_id):
                    QtWidgets.QMessageBox.information(self, "提示", "删除成功！")
                    self.edit_type_id.clear()
                    self.edit_type_name.clear()
                    self.edeit_desc.clear()
                else:
                    QtWidgets.QMessageBox.warning(self, "警告", "删除失败！")
            else:
                QtWidgets.QMessageBox.warning(self, "警告", "请输入类别代码！")
        else:
            pass
        # 刷新列表
        self.search_type()

    def type_form(self):
        """
        获取类别信息
        :return:
        """
        self.edit_type_id.setText(self.tab_type_info.item(self.tab_type_info.currentRow(), 0).text())
        self.edit_type_name.setText(self.tab_type_info.item(self.tab_type_info.currentRow(), 1).text())
        self.edeit_desc.setPlainText(self.tab_type_info.item(self.tab_type_info.currentRow(), 2).text())

    def update_type(self):
        """
        修改类别信息
        :return:
        """
        # 获取类别信息
        type_id = self.edit_type_id.text()
        type_name = self.edit_type_name.text()
        desc = self.edeit_desc.toPlainText()
        # 实例化类别信息
        update_mode = FatherType(type_id, type_name, desc)
        # 调用修改函数
        # 询问是否修改
        replay = QtWidgets.QMessageBox.question(self, "提示", "确认修改该类别信息吗？",
                                                QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No,
                                                QtWidgets.QMessageBox.StandardButton.No)
        if replay == QtWidgets.QMessageBox.StandardButton.Yes:

            if update_type_father(update_mode):
                QtWidgets.QMessageBox.information(self, "提示", "修改成功！")
                self.edit_type_id.clear()
                self.edit_type_name.clear()
                self.edeit_desc.clear()
            else:
                QtWidgets.QMessageBox.warning(self, "警告", "修改失败！")
        else:
            pass
        # 刷新列表
        self.search_type()

    def reset_form(self):
        """
        重置表单
        :return:
        """
        self.edit_type_id.clear()
        self.edit_type_name.clear()
        self.edeit_desc.clear()
        self.search_type()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Form()
    ui.show()
    sys.exit(app.exec())
