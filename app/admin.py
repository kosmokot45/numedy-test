from django.contrib import admin

# Register your models here.
from .models import Worker, Item, Warehouse, Inventory


admin.site.register(Worker)
admin.site.register(Item)
admin.site.register(Warehouse)
admin.site.register(Inventory)
