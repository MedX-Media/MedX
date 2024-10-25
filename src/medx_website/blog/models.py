from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
from django_jalali.db import models as jmodels
from tinymce.models import HTMLField

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.user.username

# مدل دسته‌بندی
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# مدل تگ
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# مدل پست
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = HTMLField()
    featured_image = models.ImageField(upload_to='featured_images/', blank=True, null=True)
    publish_date = jmodels.jDateTimeField(default=timezone.now)
    read_time = models.PositiveIntegerField(default=1)
    slug = models.SlugField(unique=True, max_length=200, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    views = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        self.read_time = len(self.content.split()) // 200
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class PostView(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'ip_address')  # Ensures one view per IP per post

    def __str__(self):
        return f"{self.ip_address} viewed {self.post.title}"
