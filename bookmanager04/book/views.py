from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('ok')

def book(request,cat_id,book_id):

    # http://127.0.0.1/1/100/?a=10&b=20
    query_string=request.GET
    # print(query_string)
    a=query_string['a']
    b=query_string.get('b')
    print(a,b)

    # http://127.0.0.1/1/100/?a=10&b=20&a=666
    alist=query_string.getlist('a')
    b=query_string.get('b')
    print(alist,b)

    page=query_string.get('page',1)
    print(page)


    return HttpResponse('喜欢看书')


def login(request):
    body=request.POST
    print(body)

    return HttpResponse('login')

def weibo(request):
    body=request.body
    print(body)
    body_str=body.decode()
    print(body_str)
    import json
    body_data=json.loads(body_str)
    print(body_data)

    return HttpResponse('weibo json')