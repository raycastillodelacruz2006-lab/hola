import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={'width': 1280, 'height': 800})
        page = await context.new_page()

        # Load local HTML file
        import os
        cwd = os.getcwd()
        await page.goto(f"file://{cwd}/.html")
        await page.wait_for_timeout(2000)

        await page.screenshot(path="verification.png")
        print("Screenshot saved to verification.png")
        await browser.close()

asyncio.run(main())
