from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import *
from django.shortcuts import render
from .forms import *
from django.utils import timezone


def test1(request):
    return HttpResponse("blog/test1 응답!")

def test2(request, no):
    print('no 타입:', type(no))
    return HttpResponse(f'no:{no}')

def test3(request, year, month, day):
    return HttpResponse(f'년:{year}, 월:{month}, 일:{day}')

def test4(request):
    return render(request, 'blog/test4.html', {'score':70})

def test5(request):
    var ='''
    Miracles happen to only those who believe in them.
    Think like a man of action and act like man of thought.
    Courage is very important. Like a muscle, it is strengthened by use.
    Life is the art of drawing sufficient conclusions from insufficient premises.
    By doubting we come at the truth.
    A man that has no virtue in himself, ever envies virtue in others.
    When money speaks, the truth keeps silent.
    Better the last smile than the first laughter.
    '''
    return render(request, 'blog/test5.html', {'var':var})

def test6(request):
    d1 = timezone.now()
    d2 = timezone.datetime(2001,3,19)
    d3 = timezone.datetime(2030,3,19)
    return render(request, 'blog/test6.html', {'date1':d1, 'date2':d2, 'date3':d3})


def test7(request):
    print('요청방식 : ', request.method)
    print('GET방식으로 전달된 질의 문자열 :', request.GET)
    print('Post방식으로 전달된 질의 문자열 :', request.POST)
    print('업로드 파일 : ', request.FILES)
    return render(request, 'blog/form_test.html')


def list(request):
    post_list = Post.objects.all()
    search_key=request.GET.get("keyword")
    if search_key:
        post_list=Post.objects.filter(title_icontains=search_key)
    return render(request,'blog/list.html',{'post_all':post_list,'q':search_key})


def detail(request, id):
    post = get_object_or_404(Post, id=id)
    return HttpResponse(post.title)

def post_create(request):
    if request.method=='POST':
        form=PostModelForm(request.POST)
        if form.is_valid():
            #true, false 제공 메소드
            print(form.cleaned_data) # 내부적으로 만들어지는 메소드
            #post=Post.objects.create(**form.cleaned_data)
            post=form.save() #-> 데이터 바인딩
            return redirect(post)
    else:
        form=PostModelForm()
        return render(request,'blog/post_form.html',{'form':form})

def post_update(request,id):
    post=Post.objects.get(id=id) #필드명
    if request.method=='POST':
        form=PostModelForm(request.POST,instance=post)
        if form.is_valid():
            #true, false 제공 메소드
            print(form.cleaned_data) # 내부적으로 만들어지는 메소드
            #새로운 인스턴스를 만들어서 새로 만들어짐 -> 수정이 아님
            post=form.save() #-> 데이터 바인딩
            return redirect(post)
    else:
        #키값에 맞춰서 짠 나온다!
        form=PostModelForm(instance=post) # 인스턴스 post 값으로 넣어주세요
        return render(request,'blog/post_update.html',{'form':form})

#삭제 방법
# 모델 인스턴스.delete()
# QuerySet.delete()
def post_delete(request,id):
    post=Post.objects.get(id=id)
    if request.method=='POST':
        post.delete()
        return redirect("blog:list")
    else:
        return render(request,'blog/post_delete.html',{'post':post})  

# 1. 데이터 추출 requset.post
# 2. 유효성 검증 -> 입력페이지로 이동
# 3. 모델인스턴스.save()
# 모델명 objects.create(인자값...)

# 수정작업 로직
# 1. 확인 -> 2. update

