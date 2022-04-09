from django.db import models
from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    profile_pic=CloudinaryField('image')
    bio=HTMLField(blank=True, default='Tell us about you and your work')
    name=models.CharField(blank=True, max_length=40)
    # contact_info=models.TextField(blank=True, max_length=50)
    user=models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'