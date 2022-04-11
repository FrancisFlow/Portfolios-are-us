from django.db import models
from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.exceptions import ObjectDoesNotExist


# Create your models here.

class Profile(models.Model):
    profile_pic=CloudinaryField('image')
    bio=models.TextField()  
    name=models.CharField(blank=True, max_length=40)
    phone_number=models.IntegerField(blank=True, default=123456789)
    user=models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'
    
    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()

    
    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
    
    def update_bio(self, new_bio):
        self.bio=new_bio
        self.save()

    
    def update_image(self, user_id, new_image):
        user=User.objects.get(id=user_id)
        self.photo=new_image
        self.save()


    class Project(models.Model):
        image=CloudinaryField('image')
        project_name=models.CharField(max_length=50)
        link=models.CharField(max_length=100)
        date_posted=models.DateField(auto_now_add=True)
        user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
        technologies=models.CharField(max_length=100)
        categories=models.CharField(max_length=100)
        details= models.CharField(max_length=100)

        def __str__(self):
            return self.project_name
        
    