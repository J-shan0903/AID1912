from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# 导入Select类
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.get("")

#定位 select元素
city=driver.find_element(By.XPATH,"//select[@id='city']")
nation=driver.find_element(By.XPATH,"//select[@id='nation']")

# 对定位的元素封装成Select类型对象
mycity =Select(city)
mynation = Select(nation)

sleep(1)
# 使用索引设置选项
mycity.select_by_index(0)

# 对城市进行操作
if mycity.is_multiple==True:
    print("城市可以多选")
else:
    print("城市只能单选")

sleep(1)
mycity.select_by_value("重庆")
sleep(1)
mycity.select_by_visible_text("上海")

print("所有的城市选项：")
for i in mycity.options:
    print(i)
    print(i.text)

for j in mycity.all_selected_options:
    print("目前选中的城市：",j.text)
print("===========================")
# 是否多选
if mynation.is_multiple ==True:
    print("民族可以多选")
else:
    print("民族只能单选")

# 取消默认被选项
mynation.deselect_by_index(0)
# 选择其中的三项
mynation.select_by_index(1)
mynation.select_by_value("满族")
mynation.select_by_visible_text("哈萨克族")

# 列出所有的民族选项
for item1 in mynation.options:
    print(item1.text)

# 列出选择的名族选项
for item2 in mynation.all_selected_options:
    print(item2.text)

# 选中的第一项
first_item = mynation.first_selected_option
print("选中的第一个选项：",first_item.text)