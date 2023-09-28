import base64
from io import BytesIO
from django.shortcuts import render
from django.db.models import Sum
from matplotlib import pyplot as plt
import numpy as np

from .models import Inventory, Warehouse, Item

# Create your views here.


def index(request):
    return render(request, "index.html")


def reports(request):
    report = []
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
    lst = []
    for item in Item.objects.all():
        data = list(Inventory.objects.filter(
            item=item).values("balance"))

        for bal in data:
            lst.append(bal['balance'])

    print(lst)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.hist(lst, edgecolor='black',
            weights=np.ones_like(lst) / len(lst))
    # plt.show()

    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())

    graph = string.decode('utf-8')

    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    # ax.hist(data, edgecolor='black', weights=np.ones_like(data) / len(data))
    # plt.show()

    return render(request, "frequency.html", {'graph': graph})
