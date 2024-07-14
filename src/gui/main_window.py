from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtWidgets import (
    QDialog,
    QHBoxLayout,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from core.crawler import Crawler
from gui.settings_window import SettingsWindow


class CrawlerThread(QThread):
    update_progress = pyqtSignal(int)
    update_status = pyqtSignal(str)

    def __init__(self, url, config, webdriver):
        super().__init__()
        self.url = url
        self.config = config
        self.webdriver = webdriver

    def run(self):
        crawler = Crawler(self.webdriver, self.config)
        crawler.crawl(self.url)
        # クローリング進捗の更新やステータス更新のロジックをここに実装


class MainWindow(QMainWindow):

    def __init__(self, config, webdriver_manager):
        super().__init__()
        self.config = config
        self.webdriver_manager = webdriver_manager
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Web Crawler Tool")
        self.setGeometry(100, 100, 600, 400)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        # URL入力
        url_layout = QHBoxLayout()
        self.url_input = QLineEdit()
        url_layout.addWidget(self.url_input)
        self.start_button = QPushButton("Start Crawling")
        self.start_button.clicked.connect(self.start_crawling)
        url_layout.addWidget(self.start_button)
        layout.addLayout(url_layout)
        # プログレスバー
        self.progress_bar = QProgressBar()
        layout.addWidget(self.progress_bar)
        # ステータス表示
        self.status_text = QTextEdit()
        self.status_text.setReadOnly(True)
        layout.addWidget(self.status_text)
        # 設定ボタン
        self.settings_button = QPushButton("Settings")
        self.settings_button.clicked.connect(self.open_settings)
        layout.addWidget(self.settings_button)
        central_widget.setLayout(layout)

    def start_crawling(self):
        url = self.url_input.text()
        if not url:
            self.status_text.append("Please enter a URL")
            return
        self.crawler_thread = CrawlerThread(
            url, self.config, self.webdriver_manager.get_driver()
        )
        self.crawler_thread.update_progress.connect(self.update_progress)
        self.crawler_thread.update_status.connect(self.update_status)
        self.crawler_thread.start()

    def update_progress(self, value):
        self.progress_bar.setValue(value)

    def update_status(self, status):
        self.status_text.append(status)

    def open_settings(self):
        # 設定画面を開くロジックをここに実装
        settings_dialog = SettingsWindow(self.config)
        if settings_dialog.exec_() == QDialog.Accepted:
            # 設定が保存された場合、必要に応じて更新を行う
            self.update_from_settings()

    def update_from_settings(self):
        # 設定変更後に必要な更新処理をここに実装
        # 例: WebDriverの再初期化など
        webdriver_width = self.config.get("webdriver", "width")
        webdriver_height = self.config.get("webdriver", "height")
        self.webdriver_manager.update_window_size(webdriver_width, webdriver_height)
