from playwright.sync_api import sync_playwright

class MCPClient:
    def __init__(self, headless=True):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=headless)
        self.page = self.browser.new_page()

    def navigate(self, url):
        self.page.goto(url)

    def type(self, selector, text):
        self.page.fill(selector, text)

    def click(self, selector):
        self.page.click(selector)

    def scroll(self):
        self.page.mouse.wheel(0, 10000)  # Scroll down

    def get_html(self):
        return self.page.content()

    def close(self):
        self.browser.close()
        self.playwright.stop()
