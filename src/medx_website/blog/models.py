from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
from django_jalali.db import models as jmodels  # Importing Jalali date support
from tinymce.models import HTMLField  # Importing HTML field for rich text editing

# UserProfile model to extend Django's built-in User model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # One-to-one relationship with User
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)  # Profile picture field

    def __str__(self):
        return self.user.username  # Returns the username for string representation

# Category model for categorizing posts
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Category name must be unique

    def __str__(self):
        return self.name  # Returns the category name for string representation

# Tag model for tagging posts
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Tag name must be unique

    def __str__(self):
        return self.name  # Returns the tag name for string representation

# Post model to represent blog posts
class Post(models.Model):
    title = models.CharField(max_length=200)  # Title of the post
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Foreign key to the User model
    content = HTMLField()  # Rich text content field
    featured_image = models.ImageField(upload_to='featured_images/', blank=True, null=True)  # Optional featured image
    publish_date = jmodels.jDateTimeField(default=timezone.now)  # Jalali date and time field with default value
    read_time = models.PositiveIntegerField(default=1)  # Estimated reading time in minutes
    slug = models.SlugField(unique=True, max_length=200, blank=True)  # Unique slug for the post
    tags = models.ManyToManyField(Tag, blank=True)  # Many-to-many relationship with Tag model
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)  # Foreign key to Category model
    views = models.PositiveIntegerField(default=0) # Stores the number of views for the post, initialized to 0

    # Overriding the save method to auto-generate slug and calculate read time
    def save(self, *args, **kwargs):
        if not self.slug:  # If slug is not set, generate it from the title
            self.slug = slugify(self.title, allow_unicode=True)
        # Calculate read time based on word count (assuming 200 words per minute)
        self.read_time = len(self.content.split()) // 200
        super().save(*args, **kwargs)  # Call the superclass's save method

    def __str__(self):
        return self.title # Returns the post title for string representation

class PostView(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'ip_address')  # Ensures one view per IP per post

    def __str__(self):
        return f"{self.ip_address} viewed {self.post.title}"