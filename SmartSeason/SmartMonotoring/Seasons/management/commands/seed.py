from django.core.management.base import BaseCommand
from Seasons.models import Field, User, Update
from faker import Faker
import random
from datetime import timedelta
from django.utils import timezone

fake = Faker()


class Command(BaseCommand):
    help = "Seed database with realistic data"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding data...")

        # Clear existing data
        Update.objects.all().delete()
        Field.objects.all().delete()
        User.objects.all().delete()

        # Create Users (Agents + Admin)
        users = []

        for _ in range(3):
            user = User.objects.create(
                role='agent',
                employee_id=fake.unique.bothify(text='EMP###'),
                region=fake.city(),
                email=fake.unique.email()
            )
            users.append(user)

        # Create one admin
        admin = User.objects.create(
            role='admin',
            employee_id="ADMIN001",
            region="HQ",
            email="admin@smartseason.com"
        )

        self.stdout.write(self.style.SUCCESS("Users created"))

        # Create Fields
        fields = []
        stages = ['planted', 'growing', 'ready', 'harvested']

        for _ in range(5):
            field = Field.objects.create(
                crop_type=random.choice(["Maize", "Beans", "Wheat", "Rice"]),
                planting_date=timezone.now().date() - timedelta(days=random.randint(1, 60)),
                stage=random.choice(stages),
                agent=random.choice(users)
            )
            fields.append(field)

        self.stdout.write(self.style.SUCCESS("Fields created"))

        #Create Updates (crop progress logs)
        for _ in range(15):
            field = random.choice(fields)

            Update.objects.create(
                field=field,
                agent=field.agent,  # assign same agent
                stage=random.choice(stages),
                description=fake.sentence()
            )

        self.stdout.write(self.style.SUCCESS("Updates created"))

        self.stdout.write(self.style.SUCCESS("Seeding complete!"))