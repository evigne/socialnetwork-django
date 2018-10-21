from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save #going to save the user object (default), when saves then run the code


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE) #like foreign key to store the user that is created
    description = models.CharField(max_length=120,default='',blank=True)
    city = models.CharField(max_length=120,default='',blank=True)
    website = models.URLField(default='',blank=True)
    phone = models.CharField(max_length=120,default='',blank=True)
    image = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.user.username

def create_profile(sender,**kwargs): #creating the user profile
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

#connecting to post save signal to create user profile when the user is created
post_save.connect(create_profile,sender=User)