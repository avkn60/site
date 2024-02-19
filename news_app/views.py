from django.shortcuts import render, get_object_or_404
from .models import Post

def home_page(request):
    posts = Post.objects.all()[:4]
    return render(request, "./primary/index.html", {'posts': posts})

def news_page(request):
    posts = Post.objects.all()
    return render(request, "./primary/news.html", {'posts': posts})

def news_detail_page(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "./primary/news-detail.html", {'post': post})