from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from main.models import Community

class Family(models.Model):
    family_name = models.CharField(max_length=150, blank=True)
    location = models.CharField(max_length=30, blank=True)
    contact = models.CharField(max_length=10, blank=True)

class Profile(models.Model):
    family = models.ForeignKey(Family, on_delete=models.CASCADE, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(max_length=150)
    bio = models.TextField()
    scc = models.ForeignKey(Community, on_delete=models.CASCADE, null=True, blank=True)

    baptism = models.BooleanField(default=False)
    eucharist = models.BooleanField(default=False)
    confirmation = models.BooleanField(default=False)
    reconciliation = models.BooleanField(default=False)
    anointing_of_the_sick = models.BooleanField(default=False)
    marriage = models.BooleanField(default=False)
    holy_orders = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    last_modified = models.DateTimeField(auto_now=False, auto_now_add=True)  


    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()