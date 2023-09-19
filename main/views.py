from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
from django.shortcuts import render

from main.forms import ItemForm
from main.models import Item


def show_main(request: HttpRequest) -> HttpResponse:
    items = Item.objects.order_by("-amount").all()
    total_amt = 0
    for item in items:
        total_amt += item.amount

    context = {
        'name': 'Juan Maxwell Tanaya',
        'class': 'C',
        'inventory': items,
        'item_amt': len(items),
        'total_amt': total_amt
    }

    return render(request, "main.html", context)


def add_item(request: HttpRequest) -> HttpResponseRedirect | HttpResponse:
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "add_item.html", context)


def show_xml(request: HttpRequest) -> HttpResponse:
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_xml_by_id(request: HttpRequest, id: int) -> HttpResponse:
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json(request: HttpRequest) -> HttpResponse:
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def show_json_by_id(request: HttpRequest, id: int) -> HttpResponse:
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
