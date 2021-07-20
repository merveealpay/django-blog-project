from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models

from blog.abstract_date import AbstractDate
from blog.models import Category


class Article(AbstractDate):
    title = models.CharField(max_length=50)
    detail = RichTextField()
    image = models.ImageField(upload_to='article_images')
    slug = AutoSlugField(populate_from='title', unique=True)
    categories = models.ManyToManyField(Category, related_name='article')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')

    def __str__(self):
        return self.title
