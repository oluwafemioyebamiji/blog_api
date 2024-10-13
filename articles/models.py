from django.db import models
from  django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length = 256)
    is_published = models.BooleanField(default=True) #business

    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length = 256)
    slug = models.CharField(max_length = 256)
    is_published = models.BooleanField(default=True)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete= models.SET_NULL, null=True) # Foreign Key CASCADE, SET_NULL, DO_NOTHING
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title