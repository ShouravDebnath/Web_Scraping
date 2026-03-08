import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=False,
            slow_mo=500
        )

        context = await browser.new_context(
            viewport={"width": 1366, "height": 768},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
        )

        page = await context.new_page()

        url = "https://www.realestate.com.au/find-agent/perth---greater-region-wa"
        await page.goto(url, wait_until="networkidle", timeout=90000)
        await page.wait_for_timeout(10000)

        title = await page.title()
        html = await page.content()

        print("Title:", repr(title))
        print("URL:", page.url)
        print("HTML length:", len(html))
        print("First 1000 chars:")
        print(html[:1000])

        await page.screenshot(path="playwright_result.png", full_page=True)

        with open("playwright_result.html", "w", encoding="utf-8") as f:
            f.write(html)

        await browser.close()

asyncio.run(main())