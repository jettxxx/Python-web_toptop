# Generated by Django 4.0.4 on 2022-05-10 04:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0004_remove_post_video_dislikes_remove_post_video_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='root_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
