from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.db import models

from blog.models import Category


class Article(models.Model):
    title = models.CharField(max_length=50)
    detail = models.TextField()
    image = models.ImageField(upload_to='article_images')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from='title', unique=True)
    categories = models.ManyToManyField(Category, related_name='article')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')

    def __str__(self):
        return self.title
