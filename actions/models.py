from django.contrib.auth.models import User
from django.db import models
from projects.choices import related_choices


class Action(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    action = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    related = models.CharField(max_length=200, choices=related_choices)
    external_id = models.UUIDField()
