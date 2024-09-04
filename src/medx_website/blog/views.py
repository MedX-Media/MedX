from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
import os
import requests

def home(request):
    latest_post = Post.objects.latest('publish_date')
    popular_posts = Post.objects.order_by('-read_time')[:3]

    all_posts = Post.objects.order_by('-publish_date')
    paginator = Paginator(all_posts, 10)

    page_number = request.GET.get('page', 1)

    try:
        page_number = int(page_number)
        if page_number < 1:
            page_number = 1
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)

    context = {
        'latest_post': latest_post,
        'page_obj': page_obj,
        'popular_posts': popular_posts,
    }
    return render(request, 'blog/home.html', context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    latest_posts = Post.objects.order_by('-publish_date')[:3]

    context = {
        'post': post,
        'latest_posts': latest_posts,
    }
    return render(request, 'blog/post_detail.html', context)
