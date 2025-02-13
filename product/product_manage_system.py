import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView, QHeaderView

from dao.product import select_all_product


class Ui_Form(QWidget):
    def __init__(self):
        super(Ui_Form, self).__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(702, 765)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../img/整改通知.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form.setWindowIcon(icon)
        self.groupBox = QtWidgets.QGroupBox(parent=Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 70, 661, 101))
        self.groupBox.setObjectName("groupBox")
        self.s_type_id = QtWidgets.QLineEdit(parent=self.groupBox)
        self.s_type_id.setGeometry(QtCore.QRect(120, 30, 131, 21))
        self.s_type_id.setObjectName("s_type_id")
        self.s_type_name = QtWidgets.QLineEdit(parent=self.groupBox)
        self.s_type_name.setGeometry(QtCore.QRect(370, 30, 161, 21))
        self.s_type_name.setObjectName("s_type_name")
        self.pb_clear = QtWidgets.QPushButton(parent=self.groupBox)
        self.pb_clear.setGeometry(QtCore.QRect(560, 30, 75, 23))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../img/更新.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pb_clear.setIcon(icon1)
        self.pb_clear.setObjectName("pb_clear")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 81, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(280, 30, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(20, 70, 81, 16))
        self.label_7.setObjectName("label_7")
        self.s_product_id = QtWidgets.QLineEdit(parent=self.groupBox)
        self.s_product_id.setGeometry(QtCore.QRect(120, 70, 131, 21))
        self.s_product_id.setObjectName("s_product_id")
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(280, 70, 81, 16))
        self.label_8.setObjectName("label_8")
        self.s_product_name = QtWidgets.QLineEdit(parent=self.groupBox)
        self.s_product_name.setGeometry(QtCore.QRect(370, 70, 161, 21))
        self.s_product_name.setObjectName("s_product_name")
        self.pb_search = QtWidgets.QPushButton(parent=self.groupBox)
        self.pb_search.setGeometry(QtCore.QRect(560, 70, 75, 23))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../img/search.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pb_search.setIcon(icon2)
        self.pb_search.setObjectName("pb_search")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=Form)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 180, 661, 291))
        self.groupBox_2.setObjectName("groupBox_2")
        self.tab_product_info = QtWidgets.QTableWidget(parent=self.groupBox_2)
        self.tab_product_info.setGeometry(QtCore.QRect(10, 20, 641, 261))
        self.tab_product_info.setObjectName("tab_product_info")
        self.tab_product_info.setColumnCount(0)
        self.tab_product_info.setRowCount(0)
        self.groupBox_3 = QtWidgets.QGroupBox(parent=Form)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 480, 661, 271))
        self.groupBox_3.setObjectName("groupBox_3")
        self.edit_type_id = QtWidgets.QLineEdit(parent=self.groupBox_3)
        self.edit_type_id.setGeometry(QtCore.QRect(110, 30, 181, 21))
        self.edit_type_id.setObjectName("edit_type_id")
        self.edeit_desc = QtWidgets.QPlainTextEdit(parent=self.groupBox_3)
        self.edeit_desc.setGeometry(QtCore.QRect(10, 120, 641, 91))
        self.edeit_desc.setObjectName("edeit_desc")
        self.pb_modify = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pb_modify.setGeometry(QtCore.QRect(70, 230, 75, 23))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../img/modify.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pb_modify.setIcon(icon3)
        self.pb_modify.setObjectName("pb_modify")
        self.pb_reset = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pb_reset.setGeometry(QtCore.QRect(310, 230, 75, 23))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../img/reset_ico.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pb_reset.setIcon(icon4)
        self.pb_reset.setObjectName("pb_reset")
        self.pb_delet = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pb_delet.setGeometry(QtCore.QRect(520, 230, 75, 23))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../img/delete.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pb_delet.setIcon(icon5)
        self.pb_delet.setObjectName("pb_delet")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(360, 30, 81, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(10, 100, 53, 15))
        self.label_5.setObjectName("label_5")
        self.label_9 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(10, 70, 81, 16))
        self.label_9.setObjectName("label_9")
        self.edit_product_id = QtWidgets.QLineEdit(parent=self.groupBox_3)
        self.edit_product_id.setGeometry(QtCore.QRect(110, 70, 181, 21))
        self.edit_product_id.setObjectName("edit_product_id")
        self.label_10 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(360, 70, 81, 16))
        self.label_10.setObjectName("label_10")
        self.edit_product_name = QtWidgets.QLineEdit(parent=self.groupBox_3)
        self.edit_product_name.setGeometry(QtCore.QRect(470, 70, 181, 21))
        self.edit_product_name.setObjectName("edit_product_name")
        self.cb_type = QtWidgets.QComboBox(parent=self.groupBox_3)
        self.cb_type.setGeometry(QtCore.QRect(470, 30, 181, 22))
        self.cb_type.setObjectName("cb_type")
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
        Form.setWindowTitle(_translate("Form", "产品信息维护系统"))
        self.groupBox.setTitle(_translate("Form", "产品类别搜索"))
        self.pb_clear.setText(_translate("Form", "清除"))
        self.label.setText(_translate("Form", "产品类别代码："))
        self.label_2.setText(_translate("Form", "产品类别名称："))
        self.label_7.setText(_translate("Form", "产品代码："))
        self.label_8.setText(_translate("Form", "产品名称："))
        self.pb_search.setText(_translate("Form", "搜索"))
        self.groupBox_2.setTitle(_translate("Form", "产品类别列表"))
        self.groupBox_3.setTitle(_translate("Form", "产品类别信息维护"))
        self.pb_modify.setText(_translate("Form", "修改"))
        self.pb_reset.setText(_translate("Form", "重置"))
        self.pb_delet.setText(_translate("Form", "删除"))
        self.label_3.setText(_translate("Form", "产品类别代码:"))
        self.label_4.setText(_translate("Form", "产品类别名称："))
        self.label_5.setText(_translate("Form", "备注说明："))
        self.label_9.setText(_translate("Form", "产品代码:"))
        self.label_10.setText(_translate("Form", "产品名称："))
        self.cb_type.setPlaceholderText(_translate("Form", "选择产品类别名称"))
        self.label_6.setText(_translate("Form", "EK烘焙 产品信息维护系统"))

    def init_table(self):
        """
        初始化表格
        :return:
        """
        type_id = self.s_type_id.text()
        type_name = self.s_type_name.text()
        search_result = select_all_product(type_id=type_id, type_name=type_name)
        row = 0
        if search_result:
            row = len(search_result)
            #  设置行和列，这两个必须设置 不然不显示，而且要往前放
            self.tab_product_info.setRowCount(row)
            self.tab_product_info.setColumnCount(3)

            for i in range(row):
                for j in range(3):
                    data = QTableWidgetItem(str(search_result[i][j]))
                    self.tab_product_info.setItem(i, j, data)
            # 隐藏垂直序号，即index
            self.tab_product_info.verticalHeader().setVisible(False)
            # 禁止编辑单元格
            self.tab_product_info.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
            # 设置选择行为为按照行来选择
            self.tab_product_info.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
            # 数据列宽自动匹配表格宽度
            self.tab_product_info.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
            # 设置表头
            self.tab_product_info.setHorizontalHeaderLabels(['产品类别代码', '产品类别名称', '备注'])
        else:
            QtWidgets.QMessageBox.warning(self, "警告", "未查询到相关类别信息！")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_Form()
    window.show()
    app.exec()
