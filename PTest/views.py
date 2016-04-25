from django.shortcuts import render,render_to_response,RequestContext
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect,HttpResponse, request
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.

def indexView(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('mainView'))
    state = None
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('mainView'))
        else:
            state = 'not_exist_or_password_error'
    content = {
        'active_menu': 'main',
        'state': state,
        'user': User
    }
    return render_to_response('login.html',RequestContext(request))

def signupView(request):
    #auth_user(password=password,username=username,email=group,first_name=totalpoint,last_name=
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('mainView'))
    state = None
    if request.method == 'POST':
        password = request.POST.get('password', '')
        repeat_password = request.POST.get('repeat_password', '')
        if password == '' or repeat_password == '':
            state = 'empty'
        elif password != repeat_password:
            state = 'repeat_error'
        else:
            username = request.POST.get('username', '')
            if User.objects.filter(username=username):
                state = 'user_exist'
            else:
                new_user = User.objects.create_user(username=username, password=password,
                                                    email=request.POST.get('group', ''))
                new_user.save()
                state = 'success'
    content = {
        'active_menu': 'mainView',
        'state': state,
        'user': User,
    }
    return render_to_response('signup.html',RequestContext(request))

@login_required
def mainView(request):
    user = request.user if request.user.is_authenticated() else None
    content = {
        'active_menu': 'mainView',
        'state': None,
        'user': user,
    }
    return render(request,'main.html', content)

@login_required
def hallView(request):
    user = request.user if request.user.is_authenticated() else None
    content = {
        'active_menu': 'hallView',
        'state': None,
        'user': user,
    }
    return render(request,'hall.html', content)

@login_required
def testView(request):
    user = request.user if request.user.is_authenticated() else None
    content = {
        'active_menu': 'testView',
        'state': None,
        'user': user,
    }
    return render(request,'test.html', content)

@login_required
def beftestView(request):
    user = request.user if request.user.is_authenticated() else None
    content = {
        'active_menu': 'beftestView',
        'state': None,
        'user': user,
    }
    return render(request,'bef-test.html', content)