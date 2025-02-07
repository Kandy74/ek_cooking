import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton

class DynamicForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置主布局为垂直布局
        self.layout = QVBoxLayout(self)

        # 添加一个输入框，用于输入标签内容
        self.label_input = QLineEdit(self)
        self.label_input.setPlaceholderText("请输入标签内容")
        self.layout.addWidget(self.label_input)

        # 添加一个按钮，用于触发添加标签和输入框的操作
        self.add_button = QPushButton('添加', self)
        self.add_button.clicked.connect(self.add_row)
        self.layout.addWidget(self.add_button)

        # 设置窗口标题和大小
        self.setWindowTitle('动态添加标签和输入框')
        self.setGeometry(300, 300, 400, 300)

    def add_row(self):
        # 获取输入框中的内容
        label_text = self.label_input.text().strip()

        # 如果输入框为空，则不添加
        if not label_text:
            return

        # 创建一个水平布局，用于放置标签和输入框
        row_layout = QHBoxLayout()

        # 创建标签和输入框
        label = QLabel(label_text, self)
        line_edit = QLineEdit(self)

        # 将标签和输入框添加到水平布局中
        row_layout.addWidget(label)
        row_layout.addWidget(line_edit)

        # 将水平布局添加到主布局中
        self.layout.addLayout(row_layout)

        # 清空输入框内容
        self.label_input.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = DynamicForm()
    form.show()
    sys.exit(app.exec())