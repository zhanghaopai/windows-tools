import sys
from PyQt5.QtWidgets import QApplication
from ui.main_window import JsonToolMainWindow

if __name__ == "__main__":
    # 解决PyQt5中文显示问题（可选）
    QApplication.setStyle("Fusion")
    app = QApplication(sys.argv)

    # 启动主窗口
    main_window = JsonToolMainWindow()
    main_window.show()

    sys.exit(app.exec_())