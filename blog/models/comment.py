from django.contrib.auth.models import User
from django.db import models

from blog.abstract_date import AbstractDate
from blog.models import Article


class Comment(AbstractDate):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    article = models.ForeignKey(Article,on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()


    def __str__(self):
        return self.author.username