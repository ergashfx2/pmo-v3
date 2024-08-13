import uuid

from django.contrib.auth.models import User
from django.db import models
from .choices import *


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    position = models.CharField(max_length=150, blank=True)
    role = models.CharField(max_length=150, blank=True)
    status = models.CharField(max_length=50, choices=[('Active', 'Active'), ('Blocked', 'Blocked')], default='Active')
    phone = models.CharField(max_length=100, blank=True)
    avatar = models.ImageField(upload_to='images/', default='human.jpg', max_length=300, blank=True)
    blog = models.CharField(max_length=200, blank=True)
    department = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def block(self):
        self.status = 'Blocked'
        self.save()

    def unblock(self):
        self.status = 'Active'
        self.save()

    def get_user_role(self):
        return self.role

    def __str__(self):
        return self.get_full_name()


class Team(models.Model):
    id = models.UUIDField(default=uuid.uuid4,primary_key=True)
    name = models.CharField(max_length=200)
    users = models.ManyToManyField(User,related_name='project_team')
    external_user = models.CharField(max_length=250,blank=True)

    def __str__(self):
        return self.name
