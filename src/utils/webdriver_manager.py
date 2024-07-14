from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class WebDriverManager:
    def __init__(self):
        self.driver = None

    def setup(self):
        try:
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service)
            return True
        except Exception as e:
            print(f"WebDriver setup failed: {e}")
            return False

    def get_driver(self):
        if not self.driver:
            self.setup()
        return self.driver

    def quit(self):
        if self.driver:
            self.driver.quit()
            self.driver = None

    def update_window_size(self, width, height):
        if self.driver:
            self.driver.set_window_size(width, height)
