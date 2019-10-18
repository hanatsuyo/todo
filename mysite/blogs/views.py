from django.shortcuts import render
from .models import Blog
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login  
from django.contrib.auth.decorators import login_required # 追加
from .models import Blog,Comment
from . import forms


def index(request):
    blogs = Blog.objects.order_by('-created_datetime')
    return render(request, 'blogs/index.html', {'blogs': blogs})


def detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    comments = Comment.objects.filter(post=blog)

    if request.method == "POST": #入力フォームはPOSTなので
        form = forms.CommentForm(request.POST)
        if form.is_valid(): #もし、formの内容が正しい時は
            comment = form.save(commit=False) #formの内容はまだセーブしません！
            comment.post = blog
            comment.author = request.user
            comment.save() #ユーザーを追加したのちにセーブ
    else:
        form = forms.CommentForm()

    print(blog)

    return render(request, 'blogs/detail.html', {
        'blog': blog,
        'form': form,
        'comments': comments
        })

def users_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'blogs/users_detail.html', {'user': user})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST) # ユーザーインスタンスを作成
        if form.is_valid():
            new_user = form.save() # ユーザーインスタンスを保存
            input_username = form.cleaned_data['username']
            input_password = form.cleaned_data['password1']
            # フォームの入力値で認証できればユーザーオブジェクト、できなければNoneを返す
            new_user = authenticate(username=input_username, password=input_password)
            # 認証成功時のみ、ユーザーをログインさせる
            if new_user is not None:
                # loginメソッドは、認証ができてなくてもログインさせることができる。→上のauthenticateで認証を実行する
                login(request, new_user)
                return redirect('blogs:users_detail', pk=new_user.pk)
    else:
        form = UserCreationForm()
    return render(request, 'blogs/signup.html', {'form': form})




