from playwright.async_api import async_playwright
import asyncio

# async def render_html_to_png_bytes(html: str, width: int = 720, wait_ms: int = 100) -> bytes:
#     async with async_playwright() as p:
#         browser = await p.chromium.launch()
#         page = await browser.new_page(viewport={"width": width, "height": 10})

#         await page.set_content(html, wait_until="load")
#         # await page.evaluate("() => document.fonts.ready")  # ensure loaded
#         await page.wait_for_timeout(200)

        


#         if wait_ms:
#             await page.wait_for_timeout(wait_ms)

#         height = await page.evaluate("() => Math.ceil(document.documentElement.scrollHeight)")
#         await page.set_viewport_size({"width": width, "height": height})

#         png = await page.screenshot(full_page=True, type="png")
#         await browser.close()
#         return png
    

class Renderer_html_to_png_bytes:

    def __init__(self, sem:int = 2, width: int = 720, wait_ms: int = 100, timeout_s: int = 15):
        self.width = width
        self.wait_ms = wait_ms
        # make sure the max concurrency of rendering is sem
        self.sem = asyncio.Semaphore(sem) 
        self._p = None
        self._browser = None
        self._timeout_s = timeout_s


    # async def render(self) -> bytes:
    #     return await render_html_to_png_bytes(self.html, self.width, self.wait_ms)
    
    async def initial(self):
        if self._browser:
            return

        self._p = await async_playwright().start()
        self._browser = await self._p.chromium.launch(
            args=["--no-sandbox", "--disable-setuid-sandbox"],
        )
        
    async def close(self):
        if self._browser:
            await self._browser.close()
            self._browser = None
        if self._p:
            await self._p.stop()
            self._p = None

    async def render(self, html: str) -> bytes:
        if not self._browser:
            raise RuntimeError("Playwright 还没有启动！请重启bot以初始化。")
        
        async with self.sem:
            return await asyncio.wait_for(self._single_render(html), timeout=self._timeout_s)
        



    async def _single_render(self, html: str) -> bytes:
        context = await self._browser.new_context(
            viewport={"width": self.width, "height": 10},
        )

        page = await context.new_page()
        try:
            await page.set_content(html, wait_until="domcontentloaded")

            if self.wait_ms:
                await page.wait_for_timeout(self.wait_ms)
            await page.evaluate("""() => Promise.all(
              [...document.images].map(img =>
                img.decode ? img.decode().catch(()=>{}) : Promise.resolve()
              )
            )""")

            height = await page.evaluate("() => Math.ceil(document.documentElement.scrollHeight)")
            await page.set_viewport_size({"width": self.width, "height": height})

            return await page.screenshot(full_page=True, type="png")
        finally:
            await page.close()
            await context.close()