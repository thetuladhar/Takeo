# Generated by Django 4.2.6 on 2023-11-13 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("social", "0007_image_userprofile_imagecomment"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="email",
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
