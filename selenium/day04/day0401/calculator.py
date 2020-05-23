class Count:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    # 定义add函数
    def add(self):
        self.r1 = self.x +self.y
        return self.r1

    # 定义减法函数
    def sub(self):
        self.r2 = self.x - self.y
        return self.r2
    # mul乘法
    def mul(self):
        self.r3 = self.x * self.y
        return self.r3
    # div除法
    def div(self):
        self.r4 = self.x / self.y
        return self.r4
