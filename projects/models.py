import uuid

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from users.choices import blogs, departments
from .choices import *
from users.models import Team

class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.CharField(max_length=150)
    author = models.ManyToManyField(User, related_name='author')
    name = models.CharField(max_length=200)
    blog = models.CharField(max_length=250, choices=blogs)
    departments = models.CharField(max_length=250, choices=departments)
    size = models.CharField(max_length=200, choices=size_choices)
    level = models.CharField(max_length=200, choices=level_choices)
    speed = models.CharField(max_length=200, choices=speed_choices)
    type = models.CharField(max_length=200, choices=type_choices)
    team = models.ForeignKey(Team,on_delete=models.SET_NULL,null=True)
    description = models.TextField()
    termination = models.IntegerField(default=0)
    start_date = models.DateTimeField(auto_now=False)
    deadline = models.DateField(auto_now=False)
    budget = models.BigIntegerField()
    status = models.CharField(max_length=150, choices=status_choices)
    spent_money = models.BigIntegerField(default=0)

    def __str__(self):
        return self.name

    def update_termination(self):
        self.termination = self.termination
        self.save()

    def update_project_status(self):
        self.status = 'Jarayonda'
        self.save()

    def finish_project_status(self):
        self.status = 'Tugatilgan'
        self.save()


class Phase(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, models.CASCADE)
    name = models.CharField(max_length=250)
    termination = models.IntegerField(default=0)
    status = models.CharField(max_length=30, choices=status_choices, default='Yangi')

    def update_phase_done_percentage(self,termination):
        self.termination = termination
        self.save()

    def update_phase_name(self):
        self.name = str(self.name)
        self.save()

    def start(self):
        self.status = 'Jarayonda'
        self.save()

    def finish(self):
        self.status = 'Tugatilgan'
        self.save()

    def __str__(self):
        return self.name


class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    assigned_to = models.CharField(max_length=250)
    deadline = models.DateField()
    phase = models.ForeignKey(Phase, models.CASCADE)
    name = models.CharField(max_length=250)
    termination = models.IntegerField(default=0)
    status = models.CharField(max_length=150, choices=status_choices, default='Yangi')

    def update_task_termination(self,termination):
        self.termination = termination
        self.save()

    def update_task_name(self):
        self.name = str(self.name)
        self.save()

    def start_task(self):
        self.status = 'Jarayonda'
        self.save()

    def finish(self):
        self.status = 'Tugatilgan'
        self.save()

    def __str__(self):
        return self.name


class Document(models.Model):
    project = models.ForeignKey(Project, models.CASCADE)
    external_id = models.UUIDField()
    document = models.FileField(upload_to='', blank=True, max_length=500)
    related = models.CharField(max_length=150, choices=related_choices)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.project.name


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, models.CASCADE)
    external_id = models.UUIDField()
    comment = models.TextField()
    type = models.CharField(max_length=150, choices=comment_types)
    created_at = models.DateTimeField(auto_now=True, editable=False)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author.get_full_name()

    def update_comment(self, comment):
        self.comment = comment
        self.update_at = timezone.now()
        self.save(update_fields=['comment'])
