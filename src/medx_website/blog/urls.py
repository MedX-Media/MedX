from django.urls import path
from . import views
from .views import upload_image, search_posts

urlpatterns = [
    path("", views.home, name="home"),
    path("post/<slug:slug>/", views.post_detail, name="post_detail"),
    path("search/", search_posts, name="search_posts"),
    path("upload_image/", upload_image, name="upload_image"),
]
