from django.shortcuts import render, redirect
from .models import Post
from django.contrib import messages
from datetime import datetime
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'index.html', {'posts': posts})

def post(request,id):
    posts = Post.objects.get(id=id)
    return render(request, 'post.html', {'posts': posts})

def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        if request.POST['category'] == '':
            category = 'uncategorized'
        else:
            category = request.POST['category']
        if title == '' or body == '':
            messages.info(request, 'All fields are required.')
            return redirect('create')
        blog = Post(title=title, body=body, category=category)
        blog.save()
        return redirect('/')
    return render(request, 'create.html')

def delete(request,id):
    blog = Post.objects.get(id=id)
    blog.delete()
    return redirect('/')

def edit(request,id):
    blog  = Post.objects.get(id=id)
    return render(request, 'edit.html', {'blog': blog})

def update(request,id):
    blog = Post.objects.get(id=id)
    if request.method == 'POST':
        blog.title = request.POST['title']
        blog.body = request.POST['body']
        blog.category = request.POST['category']
        blog.date = datetime.now()
        if blog.title == '' or blog.body == '' or blog.category == '':
            messages.info(request, 'All fields are required.')
            return redirect('create')

        blog.save()
        return redirect('/post/'+id)
    return redirect('/edit/'+id)

