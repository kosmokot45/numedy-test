from typing import Any
from django.core.management.base import BaseCommand

import secrets
import random

from app.models import Worker, Warehouse, Inventory, Item
from .clear_database import clear_db
from .data import brands, models, get_balance


class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any) -> None:
        clear_db()

        for el in range(5):
            create_worker(el)
            worker_id = el + 1
            create_warehouse(el, worker_id)

        for el in range(100):
            create_items()

        for item in range(1, 101):
            balance = get_balance()
            for stock in range(1, 6):
                create_inventory(stock, item, balance)


def create_worker(name_part: int) -> None:
    Worker.objects.create(
        name=f"Ivan_{name_part}",
    )


def create_warehouse(name_part: int, worker_id: int) -> None:
    Warehouse.objects.create(
        name=f"stock_{name_part}",
        worker=Worker.objects.get(id=worker_id),
    )


def create_items() -> None:
    Item.objects.create(
        inv_num=random.randint(1, 1000),
        brand=secrets.choice(brands),
        country="Russia",
        price=random.randint(500, 1000),
        model=secrets.choice(models),
    )


def create_inventory(stock: int, item: int, balance: list[int]) -> None:
    Inventory.objects.create(
        stock=Warehouse.objects.get(id=stock),
        item=Item.objects.get(id=item),
        balance=balance[stock-1]
    )
