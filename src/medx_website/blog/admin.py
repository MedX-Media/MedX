from django.contrib import admin

from .models import Category, Post, Tag, UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "profile_picture")


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publish_date", "category", "read_time")
    list_filter = ("publish_date", "author", "tags", "category")
    search_fields = ("title", "content", "author__username")
    prepopulated_fields = {"slug": ("title",)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.groups.filter(name="نویسنده").exists():
            return qs.filter(author=request.user)
        return qs

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user
        super().save_model(request, obj, form, change)


class TagAdmin(admin.ModelAdmin):
    search_fields = ("name",)


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ("name",)


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
