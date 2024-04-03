from django.shortcuts import render, redirect
from django.http import HttpResponse,  HttpResponseServerError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.db.models import Count,Subquery, OuterRef
from django.db import connection
from .models import blog,like_blog,cmnt_blog,Bookmark_blog, Reviews
import random
# Create your views here.
def home(request):
   
    like_count_subquery = like_blog.objects.filter(blog_id=OuterRef('pk')).values('blog_id').annotate(num_likes=Count('blog_id')).values('num_likes')
    top_blogs = blog.objects.annotate(num_likes=Subquery(like_count_subquery)).order_by('-num_likes')[:6]

    blog_item= blog.objects.order_by('-id')[:6]

    all_posts = blog.objects.all()
    random_posts = random.sample(list(all_posts), k=6)
    review_items= Reviews.objects.all()
    return render(request,"home.html",{"blog_item":blog_item,"top_blogs":top_blogs,"random_posts":random_posts, "review_items":review_items})

def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        mail=request.POST.get('email')
        pwd=request.POST.get('pwd')
        cpwd=request.POST.get('c_pwd')
        check=User.objects.filter(username=uname)
        if check:
            return render(request,'signup.html',{'error':'Username is already taken!'})
        if pwd!=cpwd:
            return render(request,'signup.html',{'error':'Password does not match'})
        else:
           my_user= User.objects.create_user(username=uname,email=mail,first_name=fname,last_name=lname,password=pwd)
           my_user.save()
           return redirect('home')
        
    return render(request,"signup.html")
    
def signin(request):
    if request.method=='POST':
         uname=request.POST.get('username')
         pwd=request.POST.get('pwd')
         user=authenticate(request,username=uname,password=pwd)
         if user is not None:
             auth.login(request,user)
             return redirect('home')
         else:
             return render(request,'signin.html',{'error':'Username or password is wrong!'})
         
    return render(request,'signin.html')

def dashboard(request,uname):
        book_blog_ids=Bookmark_blog.objects.filter(user_id=uname).only("blog_id")
        for item in book_blog_ids:
            bookmark_item = blog.objects.filter(id=item.blog_id)

        blog_item= blog.objects.filter(username=uname)
        # like_item=like_blog.objects.filter(user_id=uname)
        blog_ids = like_blog.objects.filter(user_id=uname).only("blog_id")
        for item in blog_ids:
            like_item = blog.objects.filter(id=item.blog_id)

        return render(request,"dashboard.html",{"blog_item":blog_item,"bookmark_item":bookmark_item,"like_item":like_item})

def logout(request):
    auth.logout(request)
    return render(request,"home.html")

def write(request,uname):
    if request.method=='POST':

        title=request.POST.get('title')
        content=request.POST.get('content')
        set_category=request.POST.get('dropdown')
        custom_category=request.POST.get('custom')
        if(set_category=="none"):
            category=custom_category
        else:
            category=set_category
        
        blog_data= blog(title=title,content=content,category=category,username=uname)
        blog_data.save()
        return redirect('dashboard',uname=uname)
        # return HttpResponse("Blog submitted")

    return render(request,'write.html')

def full_blog(request,id):
    blog_item=blog.objects.filter(id=id)
    for item in blog_item:
        username_info=item.username
    user_item=User.objects.filter(username=username_info)
    like_count=like_blog.objects.filter(blog_id=id).count()
    check_like=like_blog.objects.filter(blog_id=id,user_id=request.user.username)
    cmnt_count=cmnt_blog.objects.filter(blog_id=id).count()
    bookmark_count=Bookmark_blog.objects.filter(blog_id=id).count()
    check_bookmark=Bookmark_blog.objects.filter(blog_id=id,user_id=request.user.username)
    return render(request,"full.html",{"blog_item":blog_item, "user_item":user_item,"like_count":like_count,"check_like":check_like,"check_bookmark":check_bookmark,"bookmark_count":bookmark_count,"cmnt_count":cmnt_count})

def category(request):
    if request.method=='POST':
        cat_name=request.POST.get('cat_name')
        blog_item=blog.objects.filter(category=cat_name)
        return render(request,"type.html",{"blog_item": blog_item})
    
def type(request,cat):
     blog_item=blog.objects.filter(category=cat)
     return render(request,"type.html",{"blog_item": blog_item})

def like(request,uname,id):
    like_exist=like_blog.objects.filter(blog_id=id,user_id=uname)
    if like_exist:
        like_exist.delete()
    else:
        blog_data=like_blog(blog_id=id,user_id=uname)
        blog_data.save()
    return redirect('full_blog',id=id)

def comment(request,id):
    cmnt_data=cmnt_blog.objects.filter(blog_id=id)
    return render(request,"cmnt.html",{"cmnt_data":cmnt_data,"id":id})

def add_comment(request,id):
    content=request.POST.get('content')
    cmnt_data=cmnt_blog(blog_id=id,content=content,user_id=request.user.username)
    cmnt_data.save()
    return redirect('comment',id=id)

def bookmark(request,uname,id):
    bookmark_exist=Bookmark_blog.objects.filter(blog_id=id,user_id=uname)
    if bookmark_exist:
        bookmark_exist.delete()
    else:
        blog_data=Bookmark_blog(blog_id=id,user_id=uname)
        blog_data.save()
    return redirect('full_blog',id=id)

def review(request,uname):
   
        content=request.POST.get('content')
        username = User.objects.get(username=uname)
        add_review= Reviews(content=content,username=username)
        add_review.save()
        return render(request,"home.html")