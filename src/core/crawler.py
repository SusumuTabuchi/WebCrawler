# import requests
from bs4 import BeautifulSoup

# from selenium import webdriver
from .category import categorize_page
from .screenshot import take_screenshot


class Crawler:
    def __init__(self, driver, config):
        self.driver = driver
        self.config = config
        self.visited_urls = set()

    def crawl(self, start_url):
        self.driver.get(start_url)
        self._process_page(start_url)

    def _process_page(self, url):
        if url in self.visited_urls:
            return
        self.visited_urls.add(url)
        # ページのHTMLを取得
        html = self.driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        # カテゴリの判定
        category = categorize_page(soup)
        # スクリーンショットの取得
        screenshot = take_screenshot(self.driver, self.config)
        # リンクの抽出とフォロー
        links = soup.find_all("a", href=True)
        for link in links:
            next_url = link["href"]
            if self._should_follow(next_url):
                self._process_page(next_url)

    def _should_follow(self, url):
        # URL追跡のルールをここで定義
        # 例: 同じドメイン内のURLのみフォロー
        return url.startswith(self.config.get("base_url"))
