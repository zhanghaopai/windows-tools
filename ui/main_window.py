from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QTextEdit, QPushButton, QListWidget, QListWidgetItem, QSplitter
)
from PyQt5.QtCore import Qt
from core.format_json import format_json_content
from core.base_functions import clear_all_content

class JsonToolMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._init_ui()  # 初始化UI
        self._bind_events()  # 绑定按钮/控件事件

    def _init_ui(self):
        """初始化窗口和布局（纯UI布局，无业务逻辑）"""
        # 基础窗口设置
        self.setWindowTitle("多功能工具 - JSON格式化")
        self.setGeometry(100, 100, 800, 600)

        # 主容器
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QHBoxLayout(main_widget)

        # 1. 左侧功能列表
        self.func_list = QListWidget()
        self.func_list.setFixedWidth(120)
        self._add_func_item("JSON格式化")
        self._add_func_item("待添加功能1")
        self._add_func_item("待添加功能2")

        # 2. 右侧内容区（输入/输出）
        self.splitter = QSplitter(Qt.Horizontal)
        self.input_edit = QTextEdit()
        self.input_edit.setPlaceholderText("请输入JSON文本...")
        self.output_edit = QTextEdit()
        self.output_edit.setReadOnly(True)
        self.splitter.addWidget(self.input_edit)
        self.splitter.addWidget(self.output_edit)
        self.splitter.setSizes([400, 400])

        # 3. 操作按钮
        self.btn_format = QPushButton("格式化JSON")
        self.btn_clear = QPushButton("清空内容")

        # 右侧布局组装
        right_layout = QVBoxLayout()
        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.btn_format)
        btn_layout.addWidget(self.btn_clear)
        right_layout.addWidget(self.splitter)
        right_layout.addLayout(btn_layout)

        # 主布局组装
        main_layout.addWidget(self.func_list)
        main_layout.addLayout(right_layout)

    def _add_func_item(self, name):
        """添加功能项到左侧列表（UI辅助方法）"""
        item = QListWidgetItem(name)
        item.setTextAlignment(Qt.AlignCenter)
        self.func_list.addItem(item)

    def _bind_events(self):
        """绑定所有控件的事件（UI与逻辑解耦）"""
        # 功能切换
        self.func_list.currentRowChanged.connect(self._switch_function)
        # JSON格式化按钮
        self.btn_format.clicked.connect(
            lambda: format_json_content(self.input_edit, self.output_edit)
        )
        # 清空按钮
        self.btn_clear.clicked.connect(
            lambda: clear_all_content(self.input_edit, self.output_edit)
        )

    def _switch_function(self, row):
        """切换功能时的UI适配（可扩展）"""
        func_name = self.func_list.item(row).text()
        self.setWindowTitle(f"多功能工具 - {func_name}")

        # 仅JSON格式化显示输入/输出，其他功能可自定义
        if func_name == "JSON格式化":
            self.input_edit.show()
            self.output_edit.show()
            self.btn_format.show()
            self.btn_clear.show()
        else:
            self.input_edit.hide()
            self.output_edit.hide()
            self.btn_format.hide()
            self.btn_clear.hide()
            # 新增功能时，在这里添加对应的UI显示逻辑