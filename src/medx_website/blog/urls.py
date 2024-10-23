from django.urls import path
from . import views
from .views import upload_image, search_posts

# URL patterns for the blog application
urlpatterns = [
    path('', views.home, name='home'),  # URL pattern for the home page
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),  # URL pattern for post detail pages, using a slug
    path('upload_image/', upload_image, name='upload_image'),  # URL pattern for image upload
]
