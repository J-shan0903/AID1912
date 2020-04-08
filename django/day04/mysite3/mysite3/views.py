from django.http import HttpResponse
from django.shortcuts import render


def test_static(request):

    return render(request, 'test_static.html')


def test_cookies(request):
    resp = HttpResponse('--哈哈哈---')
    # resp.set_cookie('username','guoxiaonao',300)
    # resp.set_cookie('user','guoxiaonao')
    username =request.COOKIES.get('username','hahahhha')
    print(username)
    print('---test-cookies---')

    resp.delete_cookie('username',)
    return resp

def set_session(request):

    request.session['uname'] ='郭小闹'

    return HttpResponse('----set session----')

def get_session(request):
    name = request.session['uname']
    return HttpResponse('---get session values is %s'%(name))