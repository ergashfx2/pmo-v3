from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from projects.models import Project,Phase,Document,Task
from .models import Action
from projects.middlewares.get_request import current_request

@receiver(signal=post_save,sender=Project)
def create_action(sender, instance, created, **kwargs):
    if created:
        print(current_request().user)

