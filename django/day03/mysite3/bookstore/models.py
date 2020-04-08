from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField("书名", max_length=50, default='',unique=True)
    # 00000.00
    price = models.DecimalField("定价", max_digits=7, decimal_places=2, default=0.0)
    market_price = models.DecimalField("零售价", max_digits=7, decimal_places=2, default=0.0)
    # 新添加字段时记住要加default值
    pub = models.CharField('出版社', max_length=200, default='')
    is_active =models.BooleanField('是否活跃',default=True)

    def __str__(self):
        return '%s_%s_%s_%s'%(self.title,self.price,self.market_price,self.pub)

class Author(models.Model):
    # 表名 bookstore_author
    name = models.CharField('姓名', max_length=20, default='')
    age = models.IntegerField('年龄', default=1)
    email = models.EmailField('邮箱', null=True)
