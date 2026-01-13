from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QHBoxLayout,
    QListWidget, QListWidgetItem, QStackedWidget
)
from PyQt5.QtCore import Qt
from ui.json_format_ui import JsonFormatUI
from ui.function1_ui import Function1UI
from ui.function2_ui import Function2UI


class JsonToolMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 功能名称与UI组件的映射
        self.function_uis = {}
        self.current_ui = None
        self._init_ui()  # 初始化UI
        self._bind_events()  # 绑定按钮/控件事件

    def _init_ui(self):
        """初始化窗口和布局（纯UI布局，无业务逻辑）"""
        # 基础窗口设置
        self.setWindowTitle("多功能工具")
        self.setGeometry(100, 100, 800, 600)

        # 主容器
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QHBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # 1. 左侧功能列表
        self.func_list = QListWidget()
        self.func_list.setFixedWidth(120)
        
        # 定义功能列表
        functions = [
            ("JSON格式化", JsonFormatUI),
            ("待添加功能1", Function1UI),
            ("待添加功能2", Function2UI),
        ]
        
        # 添加功能项并创建对应的UI组件
        for func_name, ui_class in functions:
            self._add_func_item(func_name)
            # 创建UI组件实例
            ui_instance = ui_class(self)
            self.function_uis[func_name] = ui_instance
            # 默认隐藏所有UI
            ui_instance.hide()

        # 2. 右侧内容区容器（使用堆叠布局）
        self.right_stack = QStackedWidget()
        
        # 将所有功能UI添加到堆叠容器
        for func_name, ui_instance in self.function_uis.items():
            self.right_stack.addWidget(ui_instance.get_widget())

        # 主布局组装
        main_layout.addWidget(self.func_list)
        main_layout.addWidget(self.right_stack)

        # 默认显示第一个功能
        if functions:
            self.func_list.setCurrentRow(0)
            self._switch_function(0)

    def _add_func_item(self, name):
        """添加功能项到左侧列表（UI辅助方法）"""
        item = QListWidgetItem(name)
        item.setTextAlignment(Qt.AlignCenter)
        self.func_list.addItem(item)

    def _bind_events(self):
        """绑定所有控件的事件（UI与逻辑解耦）"""
        # 功能切换
        self.func_list.currentRowChanged.connect(self._switch_function)

    def _switch_function(self, row):
        """切换功能时的UI适配（可扩展）"""
        if row < 0 or row >= self.func_list.count():
            return
            
        func_name = self.func_list.item(row).text()
        self.setWindowTitle(f"多功能工具 - {func_name}")

        # 切换到对应的UI页面
        if func_name in self.function_uis:
            ui_instance = self.function_uis[func_name]
            # 获取UI组件在堆叠容器中的索引
            index = self.right_stack.indexOf(ui_instance.get_widget())
            if index >= 0:
                self.right_stack.setCurrentIndex(index)
                self.current_ui = ui_instance