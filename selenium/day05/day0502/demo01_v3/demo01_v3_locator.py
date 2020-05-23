from selenium.webdriver.common.by import By
class Page_Register_Locator:
    def __init__(self):
        # 定位页面元素信息
        self.findname = (By.XPATH, "//input[@name='username']")
        self.findpassword = (By.XPATH, "//input[@name='password']")
        self.findmale = (By.XPATH, "//input[@name='sex']")
        self.findfemale = (By.XPATH, "//input[@name='sex'][2]")
        self.findemail = (By.XPATH, "//input[@name='email']")
        self.findprofession = (By.XPATH, "//input[@name='profession']")
        self.findfilm = (By.XPATH, "//input[@name='film']")
        self.findpainting = (By.XPATH, "//input[@name='painting']")
        self.findcomments = (By.XPATH, "//textarea")
        self.findsumbit = (By.XPATH, "//input[@name='submit']")

