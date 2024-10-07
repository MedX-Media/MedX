# Generated by Django 5.1 on 2024-09-01 13:33

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("subtitle", models.CharField(blank=True, max_length=200)),
                ("content", models.TextField()),
                (
                    "featured_image",
                    models.ImageField(
                        blank=True, null=True, upload_to="featured_images/"
                    ),
                ),
                (
                    "publish_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("read_time", models.PositiveIntegerField(default=1)),
                ("slug", models.SlugField(blank=True, max_length=200, unique=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
