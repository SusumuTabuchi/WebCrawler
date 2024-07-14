from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QComboBox,
    QDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSlider,
    QVBoxLayout,
)


class SettingsWindow(QDialog):
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Settings")
        self.setGeometry(200, 200, 400, 300)
        layout = QVBoxLayout()
        # WebDriver設定
        webdriver_layout = QHBoxLayout()
        webdriver_layout.addWidget(QLabel("WebDriver Size:"))
        self.width_input = QLineEdit(str(self.config.get("webdriver", "width")))
        self.height_input = QLineEdit(str(self.config.get("webdriver", "height")))
        webdriver_layout.addWidget(self.width_input)
        webdriver_layout.addWidget(QLabel("x"))
        webdriver_layout.addWidget(self.height_input)
        layout.addLayout(webdriver_layout)
        # スクリーンショット設定
        screenshot_layout = QHBoxLayout()
        screenshot_layout.addWidget(QLabel("Screenshot Format:"))
        self.format_combo = QComboBox()
        self.format_combo.addItems(["png", "jpg", "bmp"])
        self.format_combo.setCurrentText(self.config.get("screenshot", "format"))
        screenshot_layout.addWidget(self.format_combo)
        layout.addLayout(screenshot_layout)
        # 画質設定
        quality_layout = QHBoxLayout()
        quality_layout.addWidget(QLabel("Quality:"))
        self.quality_slider = QSlider(Qt.Horizontal)
        self.quality_slider.setRange(0, 100)
        self.quality_slider.setValue(self.config.get("screenshot", "quality"))
        quality_layout.addWidget(self.quality_slider)
        layout.addLayout(quality_layout)
        # ファイル名設定
        prefix_layout = QHBoxLayout()
        prefix_layout.addWidget(QLabel("Excel Prefix:"))
        self.excel_prefix = QLineEdit(self.config.get("output", "excel_prefix"))
        prefix_layout.addWidget(self.excel_prefix)
        layout.addLayout(prefix_layout)
        # 保存ボタン
        save_button = QPushButton("Save")
        save_button.clicked.connect(self.save_settings)
        layout.addWidget(save_button)
        self.setLayout(layout)

    def save_settings(self):
        # 設定を保存するロジックをここに実装
        self.config.set("webdriver", "width", int(self.width_input.text()))
        self.config.set("webdriver", "height", int(self.height_input.text()))
        self.config.set("screenshot", "format", self.format_combo.currentText())
        self.config.set("screenshot", "quality", self.quality_slider.value())
        self.config.set("output", "excel_prefix", self.excel_prefix.text())
        self.config.save()
        self.close()
