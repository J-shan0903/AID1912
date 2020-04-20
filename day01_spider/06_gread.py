"""
贪婪和非贪婪匹配
"""
import re

# 贪婪匹配
html = """
<div><p>如果你为门中弟子伤她一分，我便屠你满门</p></div>
<div><p>如果你为天下人损她一毫，我便杀尽天下人</p></div>
"""
# pattern = re.compile('<div><p>.*</p></div>',re.S)

# 非贪婪匹配
pattern = re.compile('<div><p>(.*?)</p></div>',re.S)
r_list = pattern.findall(html)
print(r_list)

