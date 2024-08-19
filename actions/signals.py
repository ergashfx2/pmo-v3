from django.db.models.signals import post_save
from django.dispatch import receiver
from projects.models import Project
from projects.middlewares.get_request import current_request

@receiver(signal=post_save,sender=Project)
def create_action(sender, instance, created, **kwargs):
    if created:
        print(current_request().user)

