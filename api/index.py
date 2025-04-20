from fastapi import FastAPI
from fastapi.responses import JSONResponse
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError

app = FastAPI()

@app.get("/")
async def get_kobo_99():
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)

            context = await browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                locale="zh-TW"
            )

            page = await context.new_page()
            await page.goto("https://www.kobo.com/tw/zh", timeout=60000)

            # 找第一本 spotlight 書
            # 擷取網頁信息：抓取 .spotlight-content 下的第一個元素
            spotlight = await page.query_selector(".spotlight-content")
            
            # 嘗試從 .spotlight-content 裡面抓取需要的資料
            link = await spotlight.query_selector("a")
            link_url = await link.get_attribute("href") if link else ""

            # 封面圖：抓取 img 標籤
            cover = await spotlight.query_selector("img")
            cover_url = await cover.get_attribute("src") if cover else ""
            # 如果封面圖是以 '//' 開頭，則補上 'https:'
            if cover_url.startswith('//'):
                cover_url = 'https:' + cover_url

            # 標題：抓取 h3 標籤
            title = await spotlight.query_selector("h3")
            title_text = await title.inner_text() if title else ""
            
            # 輸出爬取結果
            book_data = {
                "link": link_url,
                "cover": cover_url,
                "title": title_text
            }

            # 關閉瀏覽器
            await browser.close()

            # 返回爬取的資料
            return book_data

    except PlaywrightTimeoutError:
        return JSONResponse(content={"error": "載入 Kobo 首頁超時"}, status_code=504)
    except Exception as e:
        print("❌ 發生錯誤：", str(e))  # 本地 debug 用
        return JSONResponse(content={"error": str(e)}, status_code=500)
