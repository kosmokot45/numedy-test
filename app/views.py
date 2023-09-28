import base64
from io import BytesIO
from typing import Any
from django.shortcuts import render
from django.db.models import Sum
from matplotlib import pyplot as plt
import numpy as np

from .models import Inventory, Warehouse, Item


def index(request):
    return render(request, "index.html")


def reports(request):
    # collect report
    report: list[dict[str, Any]] = []
    for stock in Warehouse.objects.all():
        data = {"stock": stock.name,
                "sum": Inventory.objects.filter(
                    stock=stock).aggregate(Sum("balance")).get('balance__sum'),
                "items":
                list(Inventory.objects.filter(
                    stock=stock).values("item", "balance")),
                }

        report.append(data)

    return render(request, "report.html", context={'data': report})


def freqs(request):
    # collect balance data
    balance_list: list[int] = []
    for item in Item.objects.all():
        data = list(Inventory.objects.filter(
            item=item).values("balance"))

        for balance in data:
            balance_list.append(balance['balance'])

    # create hist
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.hist(balance_list, edgecolor='black',
            weights=np.ones_like(balance_list) / len(balance_list))

    # convert image to string
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())

    return render(request, "frequency.html", {'graph': string.decode('utf-8')})
