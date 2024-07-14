import sys

from PyQt5.QtWidgets import QApplication

from gui.main_window import MainWindow
from utils.config_manager import ConfigManager
from utils.webdriver_manager import WebDriverManager


def main():
    # アプリケーションの初期化
    app = QApplication(sys.argv)
    # 設定の読み込み
    config = ConfigManager()
    # WebDriverのセットアップ
    webdriver_manager = WebDriverManager()
    if not webdriver_manager.setup():
        sys.exit("WebDriverのセットアップに失敗しました。")
    # メインウィンドウの作成と表示
    main_window = MainWindow(config, webdriver_manager)
    main_window.show()
    # アプリケーションの実行
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
