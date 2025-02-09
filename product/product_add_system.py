import sys

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView, QHeaderView

from dao.product import add_product
from dao.type_father import search_type_father
from entity.product_model import ProductModel
from entity.type_father_model import FatherType


class Ui_Form(QWidget):
    def __init__(self):
        super(Ui_Form, self).__init__()
        self.setupUi(self)
        self.search_type()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(773, 767)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../img/新增.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form.setWindowIcon(icon)
        self.groupBox = QtWidgets.QGroupBox(parent=Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 70, 401, 681))
        self.groupBox.setObjectName("groupBox")
        self.s_type_id = QtWidgets.QLineEdit(parent=self.groupBox)
        self.s_type_id.setGeometry(QtCore.QRect(90, 30, 171, 21))
        self.s_type_id.setMaximumSize(QtCore.QSize(332, 16777215))
        self.s_type_id.setPlaceholderText("")
        self.s_type_id.setObjectName("s_type_id")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 81, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 71, 21))
        self.label_2.setObjectName("label_2")
        self.tab_type = QtWidgets.QTableWidget(parent=self.groupBox)
        self.tab_type.setGeometry(QtCore.QRect(20, 90, 361, 581))
        self.tab_type.setObjectName("tab_type")
        self.tab_type.setColumnCount(0)
        self.tab_type.setRowCount(0)
        # 绑定槽函数，在点击搜索按钮时，调用该函数
        self.tab_type.clicked.connect(self.show_type_info)
        self.s_type_id_2 = QtWidgets.QLineEdit(parent=self.groupBox)
        self.s_type_id_2.setGeometry(QtCore.QRect(90, 60, 171, 21))
        self.s_type_id_2.setMaximumSize(QtCore.QSize(332, 16777215))
        self.s_type_id_2.setPlaceholderText("")
        self.s_type_id_2.setObjectName("s_type_id_2")
        self.pb_search = QtWidgets.QPushButton(parent=self.groupBox)
        self.pb_search.setGeometry(QtCore.QRect(300, 60, 75, 23))
        # 绑定搜索按钮的点击事件
        self.pb_search.clicked.connect(self.search_type)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../img/search.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pb_search.setIcon(icon1)
        self.pb_search.setObjectName("pb_search")
        self.pb_clear = QtWidgets.QPushButton(parent=self.groupBox)
        self.pb_clear.setGeometry(QtCore.QRect(300, 30, 75, 23))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../img/更新.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pb_clear.setIcon(icon2)
        self.pb_clear.setObjectName("pb_clear")
        # 绑定清空按钮的点击事件
        self.pb_clear.clicked.connect(self.clear_type)
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(260, 20, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pb_add = QtWidgets.QPushButton(parent=Form)
        self.pb_add.setGeometry(QtCore.QRect(470, 720, 75, 23))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../geological_supervision_system/img/新增.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        self.pb_add.setIcon(icon3)
        self.pb_add.setObjectName("pb_add")
        # 绑定新增按钮的点击事件
        self.pb_add.clicked.connect(self.add_product)
        self.pb_reset = QtWidgets.QPushButton(parent=Form)
        self.pb_reset.setGeometry(QtCore.QRect(640, 720, 75, 23))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../../geological_supervision_system/img/reset_ico.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        self.pb_reset.setIcon(icon4)
        self.pb_reset.setObjectName("pb_reset")
        # 绑定重置按钮的点击事件
        self.pb_reset.clicked.connect(self.reset_form)
        self.groupBox_3 = QtWidgets.QGroupBox(parent=Form)
        self.groupBox_3.setGeometry(QtCore.QRect(430, 370, 321, 341))
        self.groupBox_3.setObjectName("groupBox_3")
        self.plain_product_decs = QtWidgets.QPlainTextEdit(parent=self.groupBox_3)
        self.plain_product_decs.setGeometry(QtCore.QRect(20, 90, 291, 231))
        self.plain_product_decs.setPlainText("")
        self.plain_product_decs.setObjectName("plain_product_decs")
        self.line_product_name = QtWidgets.QLineEdit(parent=self.groupBox_3)
        self.line_product_name.setGeometry(QtCore.QRect(90, 60, 221, 21))
        self.line_product_name.setMaximumSize(QtCore.QSize(332, 16777215))
        self.line_product_name.setPlaceholderText("")
        self.line_product_name.setObjectName("line_product_name")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(20, 60, 81, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(20, 30, 71, 21))
        self.label_5.setObjectName("label_5")
        self.line_product_id = QtWidgets.QLineEdit(parent=self.groupBox_3)
        self.line_product_id.setGeometry(QtCore.QRect(90, 30, 221, 21))
        self.line_product_id.setMaximumSize(QtCore.QSize(332, 16777215))
        self.line_product_id.setPlaceholderText("")
        self.line_product_id.setObjectName("line_product_id")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=Form)
        self.groupBox_2.setGeometry(QtCore.QRect(430, 70, 321, 291))
        self.groupBox_2.setObjectName("groupBox_2")
        self.plain_type_decs = QtWidgets.QPlainTextEdit(parent=self.groupBox_2)
        self.plain_type_decs.setGeometry(QtCore.QRect(10, 20, 301, 261))
        self.plain_type_decs.setPlaceholderText("")
        self.plain_type_decs.setObjectName("plain_type_decs")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.s_type_id, self.s_type_id_2)
        Form.setTabOrder(self.s_type_id_2, self.pb_clear)
        Form.setTabOrder(self.pb_clear, self.pb_search)
        Form.setTabOrder(self.pb_search, self.plain_type_decs)
        Form.setTabOrder(self.plain_type_decs, self.line_product_id)
        Form.setTabOrder(self.line_product_id, self.line_product_name)
        Form.setTabOrder(self.line_product_name, self.plain_product_decs)
        Form.setTabOrder(self.plain_product_decs, self.pb_add)
        Form.setTabOrder(self.pb_add, self.pb_reset)
        Form.setTabOrder(self.pb_reset, self.tab_type)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "产品添加系统"))
        self.groupBox.setTitle(_translate("Form", "产品类别"))
        self.label.setText(_translate("Form", "类别代码："))
        self.label_2.setText(_translate("Form", "类别名称："))
        self.pb_search.setText(_translate("Form", "搜索"))
        self.pb_clear.setText(_translate("Form", "清空"))
        self.label_3.setText(_translate("Form", "EK烘焙 产品添加系统"))
        self.pb_add.setText(_translate("Form", "添加"))
        self.pb_reset.setText(_translate("Form", "重置"))
        self.groupBox_3.setTitle(_translate("Form", "产品添加"))
        self.plain_product_decs.setPlaceholderText(_translate("Form", "备注说明："))
        self.label_4.setText(_translate("Form", "产品名称："))
        self.label_5.setText(_translate("Form", "产品代码："))
        self.groupBox_2.setTitle(_translate("Form", "产品类别信息"))
        self.plain_type_decs.setPlainText(_translate("Form", "您所选择的产品类别代码：\n"
                                                             "产品类别名称：\n"
                                                             "备注说明："))

    def search_type(self):
        """
        搜索类别信息
        :return:
        """
        type_id = self.s_type_id.text()
        type_name = self.s_type_id_2.text()
        search_result = search_type_father(type_id=type_id, type_name=type_name)
        row = 0
        if search_result:
            row = len(search_result)
            #  设置行和列，这两个必须设置 不然不显示，而且要往前放
            self.tab_type.setRowCount(row)
            self.tab_type.setColumnCount(3)

            for i in range(row):
                for j in range(3):
                    data = QTableWidgetItem(str(search_result[i][j]))
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
        else:
            QtWidgets.QMessageBox.warning(self, "警告", "未查询到相关类别信息！")

    def clear_type(self):
        """
        清空类别信息
        :return:
        """
        self.s_type_id.clear()
        self.s_type_id_2.clear()
        self.search_type()

    def show_type_info(self):
        """
        在self.plain_type_decs中显示类别信息
        :return:
        """
        type_id = self.tab_type.item(self.tab_type.currentRow(), 0).text()
        type_name = self.tab_type.item(self.tab_type.currentRow(), 1).text()
        type_decs = self.tab_type.item(self.tab_type.currentRow(), 2).text()
        self.plain_type_decs.setPlainText("您所选择的产品类别代码：" + type_id + "\n"
                                                                                "产品类别名称：" + type_name + "\n"
                                                                                                              "备注说明：\n" + type_decs)
        # 产品代码先填写类别代码
        self.line_product_id.setText(type_id)

    def add_product(self):
        """
        添加产品信息
        :return:
        """
        product_id = self.line_product_id.text()
        type_id = self.tab_type.item(self.tab_type.currentRow(), 0).text()
        product_name = self.line_product_name.text()
        product_decs = self.plain_product_decs.toPlainText()
        type_name = self.tab_type.item(self.tab_type.currentRow(), 1).text()
        if len(product_id) == 4 or len(product_id) == 0:
            QtWidgets.QMessageBox.warning(self, "警告", "请填写产品代码！")
        elif product_name == "":
            QtWidgets.QMessageBox.warning(self, "警告", "请填写产品名称！")
        else:
            if QtWidgets.QMessageBox.question(self, "提示", "是否确认添加该产品信息？",
                                              QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No,
                                              QtWidgets.QMessageBox.StandardButton.No) == QtWidgets.QMessageBox.StandardButton.Yes:
                # 调用dao层的add_product函数，添加产品信息
                product_add = ProductModel(product_id=product_id, type_id=type_id, product_name=product_name,
                                           product_desc=product_decs, type_name=type_name)
                result = add_product(product_add)
                if result:
                    QtWidgets.QMessageBox.information(self, "提示", "添加成功！")
                else:
                    QtWidgets.QMessageBox.warning(self, "警告", "添加失败！可能代码重复！联系你老公！")

    def reset_form(self):
        """
        重置产品信息
        :return:
        """
        self.line_product_id.clear()
        self.line_product_name.clear()
        self.plain_product_decs.clear()
        self.search_type()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Form()
    ui.show()
    sys.exit(app.exec())
