from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tithe(models.Model):
    member_name = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    last_modified = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.member_name.username



class Community(models.Model):
    name = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    bio = models.TextField()

    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    last_modified = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name