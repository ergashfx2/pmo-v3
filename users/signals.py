from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user_id=instance)

@receiver(post_delete, sender=Profile)
def delete_user(sender, instance, **kwargs):
    print(instance.pk)
    User.objects.get(pk=instance.user_id.id).delete()
