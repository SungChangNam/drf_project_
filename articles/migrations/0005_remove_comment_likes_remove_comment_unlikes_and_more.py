# Generated by Django 4.1.5 on 2023-02-17 08:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0004_comment_likes_comment_unlikes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='unlikes',
        ),
        migrations.AddField(
            model_name='article',
            name='likes',
            field=models.ManyToManyField(related_name='likes_articles', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='article',
            name='unlikes',
            field=models.ManyToManyField(related_name='unlikes_articles', to=settings.AUTH_USER_MODEL),
        ),
    ]