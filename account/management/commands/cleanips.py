from django.core.management.base import BaseCommand
from account.models import BlockedIps


class Command(BaseCommand):
    help = "Used to delete ips"
    requires_migrations_checks = True
    stealth_options = ("stdin",)

    def handle(self, *args, **options):
        ips = BlockedIps.objects.all()
        ips.delete()