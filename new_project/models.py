from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class New(models.Model):
    class Status(models.TextChoices):
        DRAFT = "DT", "Draft"
        PUBLISHED = "PB", "Published"

    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120)
    body = models.TextField()
    image = models.ImageField(upload_to="news/image/")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(default=timezone.now) 
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-published_at"]

    def __str__(self):
        return self.title


class Contacts(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email

