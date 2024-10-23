from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
import os
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

@csrf_exempt
def upload_image(request):
    if request.method == 'POST':
        if request.FILES.get('file'):
            image = request.FILES['file']
            image_name = image.name
            save_path = os.path.join(settings.MEDIA_ROOT, 'uploads', image_name)
            path = default_storage.save(save_path, ContentFile(image.read()))
            image_url = os.path.join(settings.MEDIA_URL, 'uploads', image_name)
            return JsonResponse({'location': image_url})
    return JsonResponse({'error': 'Image upload failed'}, status=400)

def home(request):
    latest_post = Post.objects.latest('publish_date')
    popular_posts = Post.objects.order_by('-read_time')[:3]

    all_posts = Post.objects.order_by('-publish_date')
    paginator = Paginator(all_posts, 9)

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
    return render(request, 'main/home.html', context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    latest_posts = Post.objects.order_by('-publish_date')[:3]

    context = {
        'post': post,
        'latest_posts': latest_posts,
    }
    return render(request, 'blog/post_detail.html', context)

def search_posts(request):
    query = request.GET.get("q", "")
    page = int(request.GET.get("page", 1))
    results_per_page = 10  # Number of results per page
    start = (page - 1) * results_per_page
    end = start + results_per_page

    # Filter posts by title
    posts = Post.objects.filter(title__icontains=query)

    total_results = posts.count()
    total_pages = (
        total_results + results_per_page - 1
    ) // results_per_page  # Calculate the number of pages

    # Return the current results and add the slug
    current_results = posts[start:end].values(
        "slug", "title", "featured_image", "publish_date", "author__username"
    )

    # Convert date to string format
    response_data = {
        "results": [
            {
                "slug": post["slug"],  # Adding slug to the results dictionary
                "title": post["title"],
                "featured_image": (
                    post["featured_image"] if post["featured_image"] else None
                ),  # Check for image existence
                "publish_date": post["publish_date"].strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),  # Change this line
                "author_username": post["author__username"],
            }
            for post in current_results
        ],
        "total_pages": total_pages,
    }

    return JsonResponse(response_data)
