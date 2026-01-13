from PyQt5.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton, QSplitter
)
from PyQt5.QtCore import Qt
from ui.base_function_ui import BaseFunctionUI
from core.format_json import format_json_content
from core.base_functions import clear_all_content


class JsonFormatUI(BaseFunctionUI):
    """JSON格式化功能的UI组件"""
    
    def _init_ui(self):
        """初始化JSON格式化功能的UI布局"""
        layout = QVBoxLayout(self.widget)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # 输入/输出区域
        self.splitter = QSplitter(Qt.Horizontal)
        self.input_edit = QTextEdit()
        self.input_edit.setPlaceholderText("请输入JSON文本...")
        self.output_edit = QTextEdit()
        self.output_edit.setReadOnly(True)
        self.splitter.addWidget(self.input_edit)
        self.splitter.addWidget(self.output_edit)
        self.splitter.setSizes([400, 400])
        
        # 操作按钮
        self.btn_format = QPushButton("格式化JSON")
        self.btn_clear = QPushButton("清空内容")
        
        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.btn_format)
        btn_layout.addWidget(self.btn_clear)
        
        layout.addWidget(self.splitter)
        layout.addLayout(btn_layout)
    
    def _bind_events(self):
        """绑定JSON格式化功能的事件"""
        # JSON格式化按钮
        self.btn_format.clicked.connect(
            lambda: format_json_content(self.input_edit, self.output_edit)
        )
        # 清空按钮
        self.btn_clear.clicked.connect(
            lambda: clear_all_content(self.input_edit, self.output_edit)
        )

