class MyPage:
    # 构造函数
    def __init__(self, driver):
        self.driver = driver

    # 打开浏览器
    def open(self, url):
        base_url = url
        self.driver.get(base_url)

    # 关闭浏览器
    def bye_bye(self):
        self.driver.quit()
