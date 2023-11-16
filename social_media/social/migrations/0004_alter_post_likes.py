# Generated by Django 4.2.6 on 2023-11-08 22:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("social", "0003_alter_post_likes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="likes",
            field=models.ManyToManyField(
                default=10, related_name="liked_posts", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
