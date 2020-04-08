from django.contrib import admin

# Register your models here.

from .models import Book, Author


# 在对应的应用中的admim.py文件中进行相应的注册，有与之对应的模型类
# 与之管理类进行关联，设置表头，自定义的通过书名跳转到详情页，添加过滤器，模糊搜索，经常对某个字段进行修改
class BookMamager(admin.ModelAdmin):
    list_display = ['id', 'title', 'pub', 'price']
    list_display_links = ['title']
    list_filter = ['pub']
    search_fields = ['title', 'pub', 'price']
    list_editable = ['price']


class AuthorMamager(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'email']
    list_display_links = ['name']
    list_filter = ['name']
    search_fields = ['name']


admin.site.register(Author, AuthorMamager)
admin.site.register(Book, BookMamager)
