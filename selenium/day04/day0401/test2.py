from day04.day0401.calculator import Count

mytest = Count(10.56,23.43)
res2 = mytest.add()
if abs(res2 -33.99)<=0.001:
    print("计算正确！")
else:
    print("计算错误")
print("计算实际结果：",res2)
