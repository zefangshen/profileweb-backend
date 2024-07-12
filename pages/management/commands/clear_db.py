from typing import Any
from django.core.management.base import BaseCommand
from pages.models import Person
from utils.test import fake_image


class Command(BaseCommand):
    help = 'clear the entire database'

    def handle(self, *args: Any, **options: Any) -> str | None:
        Person.objects.all().delete()
        pass
