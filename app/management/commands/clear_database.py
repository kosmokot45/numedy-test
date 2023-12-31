from typing import Any
from django.core.management.base import BaseCommand
from app.models import Worker, Warehouse, Item, Inventory


def clear_db() -> None:
    Inventory.objects.all().delete()
    Item.objects.all().delete()
    Warehouse.objects.all().delete()
    Worker.objects.all().delete()


class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any) -> None:
        clear_db()
