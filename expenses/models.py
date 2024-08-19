import uuid
from projects.choices import related_choices
from django.db import models
from django.utils import timezone


class Expense(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    quantity = models.BigIntegerField()
    related = models.CharField(max_length=250,choices=related_choices)
    date = models.DateField(default=timezone.now)
    description = models.TextField(blank=True)
    external_id = models.UUIDField()

    def __str__(self):
        return self.related
