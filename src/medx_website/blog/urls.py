from django.urls import path

from . import views
from .views import upload_image

urlpatterns = [
    path("", views.home, name="home"),
    path("post/<slug:slug>/", views.post_detail, name="post_detail"),
    path("upload_image/", upload_image, name="upload_image"),
]
