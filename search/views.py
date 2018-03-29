from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.encoding import smart_str
from .info import *
from urllib.parse import unquote

import json

# Create your views here


def index(request):
    if request.method == 'GET':
        return render(request, 'search/index.html')

def result(request):

    print(request.method)
    if request.method == 'GET':
        
        response = None

        params = {
            'word':request.GET.get('word','车'),
            'num':'40',
        }
        
        params['start'] = request.GET.get('start', '0')
        params['source'] = request.GET.get('source', '0')

        context = ModelInfo(INFO_URL,params).get_context()
        pprint.pprint(params)

        if params['start'] == '0':
            response = render(request, 'search/search.html', context)
        else:
            response = HttpResponse(json.dumps(context), content_type='application/json')
        
        response.set_cookie('word', unquote(params['word']).encode('utf8'))
        return response

    if request.method =='POST':
        # print("ddddd")
        return render(request, 'search/index.html')

    # HttpResponse()
def login(request):

    context = {}
    word = request.COOKIES.get('word', None)
    print(type(word))

    if word is not None:
        word = word[2:-1]
        word = word.split('\\x')
        word.pop(0)
        word = map(lambda x:int(x, 16), word)
        word = bytes(word).decode()
        print(word)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            if word is not None:
                return HttpResponseRedirect('/search/results?word={0}'.format(word))
            return HttpResponseRedirect(reverse('search:search'))
        else:
            return render(request, 'search/login.html', {'UserExist':False})
    else:
        if request.user.is_authenticated:
            auth.logout(request)
            if word is not None:
                return HttpResponseRedirect('/search/results?word={0}'.format(word))
            return HttpResponseRedirect(reverse('search:search'))
        else:    
            return render(request, 'search/login.html')


def register(request):

    context = {}

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username = username)
        print(user)
        if user is not None:
            context['UserExist'] = True
            return render(request, 'search/register.html', context)
        
        user = User.objects.create_user(username = username, password = password)
        user.save()
        request.session['username'] = username
        return HttpResponseRedirect(reverse('search:login'))
    else:   
        return render(request, 'search/register.html')