from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
User = get_user_model()
from faker import Faker
fake = Faker()



class Command(BaseCommand):
    help = "Used to create fake users."
    requires_migrations_checks = True
    stealth_options = ("stdin",)

    def add_arguments(self, parser):
        parser.add_argument('--number', type=int)
        return super().add_arguments(parser)

    def handle(self, *args, **options):
        for i in range(options['number']):
            print(f'{i} user created!')
            User.objects.create_user(
                username=fake.name(),
                email=fake.email(),
                is_active=False
            )