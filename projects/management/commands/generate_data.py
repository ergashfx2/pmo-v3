import random
import uuid
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from faker import Faker
from users.choices import departments_single,blogs_single
from projects.models import Project
from users.models import Profile, Team
from expenses.models import Expense

class Command(BaseCommand):
    help = 'Generate fake data for Projects, Profiles, and Teams'

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(50):
            quantity = fake.random_int(1000000,100000000)
            related = fake.random_element(elements=('project','phase','task'))
            date = fake.date_time_this_year(before_now=True,after_now=True)
            description = fake.texts(max_nb_chars=250)
            external_id = uuid.uuid4()
            Expense.objects.create(quantity=quantity,related=related,date=date,description=description,external_id=external_id)
