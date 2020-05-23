
class MyOne:
    def first(self):
        str1 = input("请输入3个数据，以空格分割：")
        str2 = str1.split(" ")
        print(str2)
        return str2
    def second(self):
        data1 =input("请输入1个数据：")
        return data1
    def third(self):
        f = self.first()
        s = self.second()
        if s in f:
            print("包含")
        else:
            print("不包含")

if __name__ == '__main__':
    m =MyOne()
    m.third()