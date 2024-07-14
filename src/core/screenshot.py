import io

from PIL import Image


def take_screenshot(driver, config):
    # スクリーンショットを取得
    png = driver.get_screenshot_as_png()
    img = Image.open(io.BytesIO(png))
    # 設定に基づいて画像を処理
    format = config.get("screenshot", "format")
    quality = config.get("screenshot", "quality")
    # 画像をメモリ上で処理
    output = io.BytesIO()
    img.save(output, format=format, quality=quality)
    return output.getvalue()
