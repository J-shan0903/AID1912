from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep


class MyCommments():
    # 构造函数
    def __init__(self,driver):
        self.driver = driver


    # 打开浏览器
    def open(self, url):
        base_url = url
        self.driver.get(base_url)

    # 输入姓名
    def type_name(self, n):
        name = self.driver.find_element(By.XPATH, "//input[@name='username']")
        name.send_keys(n)

    # 输入密码
    def type_password(self, p):
        password = self.driver.find_element(By.XPATH, "//input[@name='password']")
        password.send_keys(p)

    # 点击性别男
    def click_male(self):
        male = self.driver.find_element(By.XPATH, "//input[@name='sex']")
        male.click()

    # 点击性别女
    def click_female(self):
        female = self.driver.find_element(By.XPATH, "//input[@name='sex'][2]")
        female.click()

    # 输入邮箱
    def type_email(self, e):
        email = self.driver.find_element(By.XPATH, "//input[@name='email']")
        email.send_keys(e)

    # 选择专业
    def select_profession(self, t):
        profession = self.driver.find_element(By.XPATH, "//input[@name='profession']")
        p1 = Select(profession)
        p1.select_by_visible_text(t)

    # 选择爱好（6个）

    # 点击影视娱乐
    def click_film(self):
        film = self.driver.find_element(By.XPATH, "//input[@name='film']")
        if film.is_selected() == False:
            film.click()

    # 点击绘画书法
    def click_painting(self):
        painting = self.driver.find_element(By.XPATH, "//input[@name='painting']")
        if painting.is_selected() == False:
            painting.click()

    # 输入留言
    def type_comment(self, c):
        comments = self.driver.find_element(By.XPATH, "//textarea")
        comments.send_keys(c)

    # 点击提交
    def click_submit(self):
        submit = self.driver.find_element(By.XPATH, "//input[@name='submit']")
        submit.click()

    # 关闭浏览器
    def bye_bye(self):
        self.driver.quit()


if __name__ == '__main__':
    driver = webdriver.Chrome()
    # 打开页面
    base_url = ""
    test = MyCommments()
    test.open(base_url)
    # 测试数据
    myname = ["张三", "王晓明", "黎明"]
    mypassword = ["abcdef", "123456", "zxd"]
    mymail = ["xiaoming@126.com", "Tom@126.com", "liming@126.com"]
    myprofession = ["法律相关", "艺术/设计", "教育/研究"]
    mycomments = ["你好", "软件测试工程师", "selenium"]

    for name, password, email, profession, comments in zip(myname, mypassword, mymail, myprofession, mycomments):
        test.type_name(name)
        test.type_password(password)
        test.click_female()
        test.type_email(email)
        test.select_profession(profession)
        test.click_film()
        test.click_painting()
        test.type_comment(comments)
        sleep(1)
        test.click_submit()
    test.bye_bye()



