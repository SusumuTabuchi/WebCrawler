# from bs4 import BeautifulSoup


def categorize_page(soup):
    # この関数はページの内容を分析し、カテゴリを決定します
    # 実際の実装はウェブサイトの構造に依存します
    # 例: タイトルとメタタグを使用してカテゴリを推測
    title = soup.title.string if soup.title else ""
    meta_description = soup.find("meta", attrs={"name": "description"})
    description = meta_description["content"] if meta_description else ""
    # カテゴリ判定ロジック（簡略化例）
    if "product" in title.lower() or "product" in description.lower():
        return "Product"
    elif "blog" in title.lower() or "article" in title.lower():
        return "Blog"
    elif "about" in title.lower() or "company" in title.lower():
        return "About"
    else:
        return "Others"
