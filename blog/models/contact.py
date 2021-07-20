from django.contrib.auth.models import User
from django.db import models


class Contact(models.Model):
    email = models.EmailField(max_length=200)
    name_surname = models.CharField(max_length=150)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
