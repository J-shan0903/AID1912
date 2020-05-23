# 导入模块
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# 实例化Chrome类
driver = webdriver.Chrome()
# 打开测试网页
driver.get('http://127.0.0.1:8060')

# 定位页面元素
male = driver.find_element(By.ID,'male')
female = driver.find_element(By.ID,'female')

wangyin  = driver.find_element(By.ID,'wangyin')
weixin  = driver.find_element(By.ID,'weixin')
zhifubao = driver.find_element(By.ID,'zhifubao')
baiduqianbao  = driver.find_element(By.ID,'baiduqianbao')

music  = driver.find_element(By.ID,'music')
mounting  = driver.find_element(By.ID,'mounting')
travel = driver.find_element(By.ID,'travel')
reading  = driver.find_element(By.ID,'readng')

tishi1 =driver.find_element(By.ID,'xianbie')
tishi2 =driver.find_element(By.ID,'zhifu')
tishi3 =driver.find_element(By.ID,'aihao')
# 判断性别选中项
if male.is_selected():
    print('性别选择的是：',male.get_attribute("value"))
elif female.is_selected():
    f = female.get_attribute("value")
    print('性别选择的是：',f)


# 支付方式：点击微信、百度钱包，判断最终选择的支付方式
sleep(1)
weixin.click()
sleep(1)
baiduqianbao.click()
'''
if wangyin.is_enabled():
    print("支付方式选择的是:",wangyin.get_attribute("value"))
elif weixin.is_enabled():
    print("支付方式选择的是:",weixin.get_attribute("value")) 
elif zhifubao.is_enabled():
    print("支付方式选择的是:",zhifubao.get_attribute("value")) 
elif baiduqianbao.is_enabled():
    print("支付方式选择的是:",baiduqianbao.get_attribute("value")) 
else:
    print("没有选择支付方式")
'''
zhifu = driver.find_elements(By.NAME,"psy")

for i in zhifu:
    if i.is_selected():
        print("支付方式选择的是:", i.get_attribute("value"))

# 兴趣爱好：点击爬山和阅读，输出选中的爱好
sleep(1)
mounting.click()
sleep(1)
reading.click()
# 获取复选框的选择情况，放在列表中
xingqu1 =[music.is_selected(),mounting.is_selected(),travel.is_selected(),reading.is_selected()]
# 获取复选框的value，放在列表中
xingqu2 = [music.get_attribute("value"),mounting.get_attribute("value"),travel.get_attribute("value"),reading.get_attribute("value")]

str1 ="兴趣爱好选择"
for item1,item2 in zip(xingqu1,xingqu2):
    if item1 ==True:
        str1 = str1 + item2+" "
print(str1)
# 取出静态文本内容
text =[tishi1.text,tishi2.text,tishi3.text]
print(text)