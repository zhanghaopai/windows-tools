from PyQt5.QtWidgets import QWidget
from abc import ABC, abstractmethod


class BaseFunctionUI(ABC):
    """功能UI基类，所有功能的UI组件都应继承此类"""
    
    def __init__(self, parent=None):
        self.parent = parent
        self.widget = QWidget(parent)
        self._init_ui()
        self._bind_events()
    
    @abstractmethod
    def _init_ui(self):
        """初始化UI布局（子类必须实现）"""
        pass
    
    @abstractmethod
    def _bind_events(self):
        """绑定事件（子类必须实现）"""
        pass
    
    def show(self):
        """显示UI组件"""
        self.widget.show()
    
    def hide(self):
        """隐藏UI组件"""
        self.widget.hide()
    
    def get_widget(self):
        """获取UI组件widget"""
        return self.widget

