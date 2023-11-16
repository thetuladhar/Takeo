# Generated by Django 4.2.6 on 2023-11-13 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("social", "0013_alter_userprofile_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="bio",
            field=models.TextField(default="No Bio Available"),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="location",
            field=models.CharField(default="Location not specified", max_length=100),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="profile_picture",
            field=models.ImageField(
                default="images/profile_pictures/default.png",
                upload_to="images/profile_pictures",
            ),
        ),
    ]