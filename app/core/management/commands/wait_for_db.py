"""
Django command to wait for the database
"""
from typing import Any, Optional
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for db"""

    def handle(self, *args, **options):
        pass
