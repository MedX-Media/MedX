from django.apps import AppConfig

# Configuration class for the Blog application
class BlogConfig(AppConfig):
    # Specifies the default field type for auto-generated primary keys
    default_auto_field = 'django.db.models.BigAutoField'
    # The name of the application
    name = 'blog'
