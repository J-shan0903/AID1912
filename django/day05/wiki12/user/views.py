from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import User
import hashlib

# Create your views here.

def reg_view(request):
    if request.method == 'GET':
        return render(request, 'user/regiter.html')
    elif request.method == 'POST':

        username = request.POST.get('username')
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')

        if password_1 != password_2:
            return HttpResponse('The password is not same')

        old_users = User.objects.filter(username=username)
        if old_users:
            return HttpResponse('The username is already existed')


        m = hashlib.md5()
        m.update(password_1.encode())
        password_h = m.hexdigest()

        try:
            user = User.objects.create(username=username, password=password_h)

        except Exception as e:
            print('--create error', e)
            return HttpResponse('----create error---')

        request.session['uid'] = user.id
        request.session['username'] = username

        return HttpResponse('---register is ok---')


def login_view(request):
    if request.method == 'GET':
        if 'username' in request.session and 'uid' in request.session:
            return HttpResponse('您已登陆!')
        username =request.COOKIES.get('username')
        uid =request.COOKIES.get('uid')
        if username and uid:
            request.session['username'] = username
            request.session['uid'] = uid
            return HttpResponse('您登陆成功!')

        return render(request, 'user/login.html')
    elif request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            old_user = User.objects.create(username=username, password=password)

        except Exception as e:
            print('--create error', e)
            return HttpResponse('您输入的用户名或密码不正确')

        m = hashlib.md5()
        m.update(password.encode())
        password_h = m.hexdigest()

        if password_h !=old_user.password:
            return HttpResponse('您输入的用户名或密码不正确')

        request.session['uid'] = old_user.id
        request.session['username'] = username
        print(request.POST)
        resp =HttpResponse('login is ok')
        if 'remember' in request.POST:
            resp.set_cookie('username',username,3600*34*3)
            resp.set_cookie('uid',old_user.id,3600*34*3)
        return resp

