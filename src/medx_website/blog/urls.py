from django.urls import path  # Importing path to define URL patterns
from . import views  # Importing all views from the current package
from .views import upload_image  # Importing the specific upload_image view

# URL patterns for the blog application
urlpatterns = [
    path('', views.home, name='home'),  # URL pattern for the home page
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),  # URL pattern for post detail pages, using a slug
    path('upload_image/', upload_image, name='upload_image'),  # URL pattern for image upload
]
