from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Profile


# When a User is created it will create it's profile
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username = user.username,
            email = user.email,
            first_name = user.first_name,
            last_name = user.last_name,
        )



# When a profile is deleted it will delete user

def deleteUser(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass


post_save.connect(createProfile, sender=User)
post_delete.connect(deleteUser, sender=Profile)