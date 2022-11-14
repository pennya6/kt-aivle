from django.shortcuts import render
from django.http import HttpResponse,Http404
from models import Post

# Create your views here.

def test1(request):
    return HttpResponse("blog/test1 응답!")

def test2(request,no):
    return HttpResponse(f"no:{no}")

def test3(request,year,month,day):
    return HttpResponse(f"{year}년 {month}월 {day}일")

def list(request):
    post_list=Post.objects.all()
    titles=""
    for post in post_list:
        titles+=post.title
    return HttpResponse(titles)

def detail (requset, id):
    try:
        post=Post.objects.get(id=id)
    except Post.DoesNotExst:
        raise Http404('존재하지 않는 데이터')
    return HttpResponse(post.title)