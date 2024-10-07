from django.contrib import admin
from .models import Post, Tag, Category
from .models import UserProfile

# Registering the UserProfile model with the admin interface
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    # Specifies the fields to be displayed in the admin list view
    list_display = ('user', 'profile_picture')

# Admin configuration for the Post model
class PostAdmin(admin.ModelAdmin):
    # Specifies the fields to display in the admin list view
    list_display = ('title', 'author', 'publish_date', 'category', 'read_time')
    # Adds filters for the admin list view
    list_filter = ('publish_date', 'author', 'tags', 'category')
    # Enables searching for specific fields in the admin interface
    search_fields = ('title', 'content', 'author__username')
    # Automatically fills the slug field based on the title
    prepopulated_fields = {'slug': ('title',)}

    # Custom queryset to filter posts based on user group
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # If the user is in the 'نویسنده' group, filter to show only their posts
        if request.user.groups.filter(name='نویسنده').exists():
            return qs.filter(author=request.user)
        return qs

    # Override save_model to automatically set the author to the logged-in user
    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Check if the object is being created
            obj.author = request.user  # Set the author to the logged-in user
        super().save_model(request, obj, form, change)  # Call the superclass's save method

# Admin configuration for the Tag model
class TagAdmin(admin.ModelAdmin):
    # Enables searching for tags by name
    search_fields = ('name',)

# Admin configuration for the Category model
class CategoryAdmin(admin.ModelAdmin):
    # Enables searching for categories by name
    search_fields = ('name',)

# Registering the Post, Tag, and Category models with their respective admin configurations
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
