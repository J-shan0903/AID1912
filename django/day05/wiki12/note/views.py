from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

def check_login(fn):
    def wrap(request,*args,**kwargs):
        if  'usernme'not in request.session or 'uid' not in request.session:
            c_username =request.COOKIES.get('username')
            c_uid =request.COOKIES.get('uid')
            if not c_username or not c_uid:
                return HttpResponseRedirect('/user/login')
            else:
                request.session['usernsme'] = c_username
                request.session['uid'] = c_uid



        return fn(request,*args,**kwargs)
    return wrap



@check_login
def add_view(request):

    return HttpResponse('开始添加笔记')