from django.http import HttpResponse
from django.shortcuts import render

def test_html(request):
    s =request.POST.get('sss')


    # from django.template import loader
    # # 1 加载html
    # t =loader.get_template('test_html.html')
    # # 2执行render 转化成字符串
    # html =t.render()
    # # 3响应给浏览器
    # return HttpResponse(html)
    dic ={
        'username':'guoxiaonao1354',
        'age':18,
        'lis':['Tom','Lili','jack'],
        'd':{
            'title':'Django'
        },
        'func':say_hi,
        'class_obj':Dog(),
        'script':'<script>alert(11)</script>'
    }
    return render(request,'test_html.html',dic)

class Dog:
    def say(self):
        return 'hahaha'


def say_hi():

    return 'Hi everyone'


def mycal_view(request):
    if request.method =='GET':
        return render(request,'mycal.html')
    elif request.method=='POST':
        # 计算数据
        x = request.POST['x']
        y = request.POST['y']
        op = request.POST['op']

        try:
            x = int(x)
            y = int(y)
        except Exception as e:
            error = 'The input is error'
            return render(request, 'mycal.html', locals())
           # return HttpResponse('The input is error')
        if op == 'add':
            result = x + y
        elif op == 'sub':
            result = x - y
        elif op == 'mul':
            result = x * y
        elif op == 'div':
            if y == 0:
                return HttpResponse('The input is error')
            result =x / y
        else:
            return HttpResponse('The op is error')

        return render(request,'mycal.html',locals())


def test_base(request):
    lst =['Tom','Jack']
    return render(request,'base.html',locals())

def test_music(request):

    return render(request,'music.html')

def test_sport(request):

    return render(request,'sport.html')



def page1_view(request):

    return render(request, 'page1.html')


def page2_view(request):

    return HttpResponse('我是page2')

def pagen_view(request, n):

    from django.urls import reverse
    print('----reverse res----')
    print(reverse('page2'))
    print(reverse('pn', kwargs={'n':500}))
    #print(reverse('pn', args=[300]))

    return HttpResponse('我是page%s'%(n))
