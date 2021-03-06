from django.http import HttpResponse,JsonResponse
from django.http import HttpResponseRedirect

post_form="""
<form method='post' action="/test_post">

    姓名:<input type="text" name="username">
    密码:<input type="text" name="pwd">
    <input type='submit' value='登陆'>
</form>
"""
def index_view(request):
    html ='<h1>这是首页</h1>'

    return HttpResponse(html)

def page1_view(request):
    html ='<h1>第一个页面</h1>'
    # return HttpResponse(html)
    
    return HttpResponseRedirect('/page2')

def page2_view(request):
    html ='<h1>第二个页面</h1>'
    return HttpResponse(html)

def pagen_view(request,n):
    html = '===这是第%s个页面===' % (n)
    return HttpResponse(html)

def cal_view(request,num1,op,num2):
    num1 =int(num1)
    num2=int(num2)
    if op not in['mul','add','sub']:
        return HttpResponse('Sorry~Your op is wrong~')
    if op =='add':
        res =num1 +num2
    elif op =='mul':
        res =num1 +num2
    else:
        res =num1 -num2
    return HttpResponse('result is %s'%(res))

def person_view(request,name,age):
    return HttpResponse('姓名：%s 年龄:%s'%(name,age))

def birthday_view(request,y,m,d):
    print(request.path_info)
    print(request.get_full_path())
    print(request.method)

    print(request.GET)
    print(request.POST)
    return HttpResponse('生日:%s年%s月%s日'%(y,m,d))


def test_get(request):
    if request.method =='GET':
        print('--test---get---')
        print(request.GET)
        # print(request.GET['a'])
        # print(request.GET.getlist('a'))
        # print(request.GET.get('b','123'))
        return HttpResponse('test get is ok')
    return HttpResponse('get is error')

def test_post(request):
    if request.method=='GET':
        html =post_form
        return HttpResponse(html)
    elif request.method=='POST':
        username = request.POST['username']
        print('--test---post--')
        print(username)
        return HttpResponse('test post is ok')

    return HttpResponse('test post is error')

