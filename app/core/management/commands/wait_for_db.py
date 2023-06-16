"""
Django command to wait for the database
"""
import time

from psycopg2 import OperationalError as Psycorpg2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for db"""

    def handle(self, *args, **options):
        """Entrypoint for command."""
        self.stdout.write("Waiting for database...")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycorpg2OpError, OperationalError):
                self.stdout.write("Database unavaiable, waiting 1 second ...")
        self.stdout.write(self.style.SUCCESS('Database available! '))

