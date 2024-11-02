from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_blog_admin = models.BooleanField(default=False)
    is_qa = models.BooleanField(default=False)

    def __str__(self):
        return self.username