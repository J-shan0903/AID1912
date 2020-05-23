from selenium import webdriver
from day05.day0502.demo01_v3.demo01_v3_register import MyCommments
# 导入csv处理csv格式的文件
import csv
from time import sleep

if __name__ == '__main__':
    driver = webdriver.Chrome()
    # 打开页面
    base_url = "页面路径"

    test = MyCommments(driver)
    test.open(base_url)
    # 测试数据
    f = open("文件路径",'r')
    data = csv.reader(f)

    for mydata in data:
        print(mydata)
        test.type_name(mydata[0])
        test.type_password(mydata[1])
        test.click_female()
        test.type_email(mydata[2])
        test.select_profession(mydata[3])
        test.click_film()
        test.click_painting()
        test.type_comment(mydata[4])
        sleep(1)
        test.click_submit()

    test.bye_bye()