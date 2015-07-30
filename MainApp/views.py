# -*- coding:utf-8 -*-a
from django.shortcuts import render
from django.shortcuts import render_to_response,render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from .login import LoginForm
from django.contrib import auth
# Create your views here.
def index(request):
    #return HttpResponse(u"Welcome, this is test page!中文测试！")
    #return render(request, 'index.html')
    return render_to_response('index.html', RequestContext(request))

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    total = int(a)+int(b)
    return HttpResponse(str(total))

# 采用 /add/3/4/ 这样的传值方式，请求参数在函数中体现
def add2(request,a,b):
    c = int(a) + int(b)
    return HttpResponse(str(c))

def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render_to_response('login.html', RequestContext(request, {'form': form,}))
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return render_to_response('index.html', RequestContext(request,{'userform': form,}))
            else:
                return render_to_response('login.html', RequestContext(request, {'form': form,'password_is_wrong':True}))
        else:
            return render_to_response('login.html', RequestContext(request, {'form': form,}))

@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/login/")