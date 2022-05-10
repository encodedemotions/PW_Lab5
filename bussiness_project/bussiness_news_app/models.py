from django.db import models
# from django.contrib.auth.models import AbstractUser, User
from datetime import datetime
from django.utils.timezone import now as now

status_select = {
    ('pedestrian', 'PEDESTRIAN'),
    ('editor', 'EDITOR')
}


class User(models.Model):

    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30, help_text='Optional.')
    last_name = models.CharField(max_length=30, help_text='Optional.')
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    status = models.CharField(max_length=10, choices=status_select, default='pedestrian')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'password', 'status']


article_permission = {
    ('public', 'PUBLIC'),
    ('private', 'PRIVATE')
}


class Posts(models.Model):

    author = models.CharField(max_length=30)
    title = models.CharField(default='Hot News', max_length=50)
    article = models.TextField()
    image = models.FileField(default=None, upload_to='images/')
    date = models.DateField(default=now)
    article_permission = models.CharField(max_length=35, choices=article_permission, default='public')

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'


# class Posts(models.Model):
#
#     author = models.CharField(max_length=30)
#     title = models.CharField(default='Hot News', max_length=100)
#     article = models.TextField()
#     image = models.FileField(default=None, upload_to='images/')
#     date = models.DateField(default=now)
#     article_permission = models.CharField(max_length=35, choices=article_permission, default='public')

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'


class AboutAuthor(models.Model):

    author = models.CharField(max_length=30)
    description = models.TextField()
    image = models.FileField(default=None, upload_to='author_image/')
    fullname = models.CharField(default=None, max_length=40)

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'
