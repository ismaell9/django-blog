from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author' : 'Corut',
        'title' : 'Blog post 1',
        'content' : 'first blog post',
        'date_posted' : 'Augest 20, 2019'
    },
    {
        'author' : 'Gwin',
        'title' : 'Blog post 2',
        'content' : 'Secone blog post',
        'date_posted' : 'Augest 25, 2019'
    }
]

def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context=context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})