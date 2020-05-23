from day05.day0502.demo01_v3.demo01_v3_locator import Page_Register_Locator
from day05.day0502.demo01_v3.demo01_v3_mypage import MyPage
from selenium.webdriver.support.select import Select

class MyCommments(MyPage):

    # 构造函数
    def __init__(self,driver):
        MyPage. __init__(self, driver)
        self.Lr =Page_Register_Locator()

    # 输入姓名
    def type_name(self, n):
        self.name = self.driver.find_element(*self.Lr.findname)
        self.name.send_keys(n)

    # 输入密码
    def type_password(self, p):
        self.password = self.driver.find_element(*self.Lr.findpassword)
        self.password.send_keys(p)

    # 点击性别男
    def click_male(self):
        self.male = self.driver.find_element(*self.Lr.findmale)
        self.male.click()

    # 点击性别女
    def click_female(self):
        self.female = self.driver.find_element(*self.Lr.findfemale)
        self.female.click()

    # 输入邮箱
    def type_email(self, e):
        self.email = self.driver.find_element(*self.Lr.findemail)
        self.email.send_keys(e)

    # 选择专业
    def select_profession(self, t):
        self.profession = self.driver.find_element(*self.Lr.findprofession)
        self.p1 = Select(self.profession)
        self.p1.select_by_visible_text(t)

    # 选择爱好（6个）

    # 点击影视娱乐
    def click_film(self):
        self.film = self.driver.find_element(*self.Lr.findfilm)
        if self.film.is_selected() == False:
            self.film.click()

    # 点击绘画书法
    def click_painting(self):
        painting = self.driver.find_element(*self.Lr.findpainting)
        if painting.is_selected() == False:
            painting.click()

    # 输入留言
    def type_comment(self, c):
        self.comments = self.driver.find_element(*self.Lr.findcomments)
        self.comments.send_keys(c)

    # 点击提交
    def click_submit(self):
        self.submit = self.driver.find_element(*self.Lr.findsumbit)
        self.submit.click()






