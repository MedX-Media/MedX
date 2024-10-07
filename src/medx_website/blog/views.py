from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  # Importing pagination classes
from django.shortcuts import render, get_object_or_404, redirect  # Importing rendering and object retrieval functions
from .models import Post  # Importing the Post model
import os  # Importing os for file path manipulation
import requests  # Importing requests for HTTP requests (not used in the code, can be removed if unnecessary)
from django.http import JsonResponse  # Importing JsonResponse for returning JSON data
from django.views.decorators.csrf import csrf_exempt  # Importing CSRF exemption decorator
from django.conf import settings  # Importing settings for project configurations
from django.core.files.storage import default_storage  # Importing default storage for file saving
from django.core.files.base import ContentFile  # Importing ContentFile for saving file content

@csrf_exempt  # Exempting this view from CSRF verification for image uploads
def upload_image(request):
    if request.method == 'POST':  # Checking if the request method is POST
        if request.FILES.get('file'):  # Checking if a file was uploaded
            image = request.FILES['file']  # Retrieving the uploaded image file
            image_name = image.name  # Getting the name of the image file
            # Defining the path to save the uploaded image
            save_path = os.path.join(settings.MEDIA_ROOT, 'uploads', image_name)
            # Saving the image to the defined path
            path = default_storage.save(save_path, ContentFile(image.read()))
            # Constructing the URL to access the uploaded image
            image_url = os.path.join(settings.MEDIA_URL, 'uploads', image_name)
            # Returning a JSON response with the image URL
            return JsonResponse({'location': image_url})
    # Returning an error response if the image upload fails
    return JsonResponse({'error': 'Image upload failed'}, status=400)

def home(request):
    # Fetching the latest post by publish date
    latest_post = Post.objects.latest('publish_date')
    # Fetching the three most popular posts based on read time
    popular_posts = Post.objects.order_by('-read_time')[:3]

    # Fetching all posts, ordered by publish date
    all_posts = Post.objects.order_by('-publish_date')
    # Setting up pagination with 9 posts per page
    paginator = Paginator(all_posts, 9)

    # Getting the page number from the query parameters, defaulting to 1
    page_number = request.GET.get('page', 1)

    try:
        page_number = int(page_number)  # Trying to convert the page number to an integer
        if page_number < 1:  # Ensuring the page number is at least 1
            page_number = 1
        page_obj = paginator.get_page(page_number)  # Getting the specific page of posts
    except PageNotAnInteger:  # Handling case where page number is not an integer
        page_obj = paginator.get_page(1)  # Default to the first page
    except EmptyPage:  # Handling case where the page number is out of range
        page_obj = paginator.get_page(paginator.num_pages)  # Get the last page

    # Context dictionary to pass data to the template
    context = {
        'latest_post': latest_post,
        'page_obj': page_obj,
        'popular_posts': popular_posts,
    }
    # Rendering the home page with the context data
    return render(request, 'main/home.html', context)

def post_detail(request, slug):
    # Fetching the specific post by its slug or returning a 404 if not found
    post = get_object_or_404(Post, slug=slug)
    # Fetching the three latest posts for the sidebar or related posts section
    latest_posts = Post.objects.order_by('-publish_date')[:3]

    # Context dictionary to pass data to the template
    context = {
        'post': post,
        'latest_posts': latest_posts,
    }
    # Rendering the post detail page with the context data
    return render(request, 'blog/post_detail.html', context)
