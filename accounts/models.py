from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save #going to save the user object (default), when saves then run the code


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE) #like foreign key to store the user that is created
    description = models.CharField(max_length=120,default='')
    city = models.CharField(max_length=120,default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)

def create_profile(sender,**kwargs): #creating the user profile
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

#connecting to post save signal to create user profile when the user is created
post_save.connect(create_profile,sender=User)