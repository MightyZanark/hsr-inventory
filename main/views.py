from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
from django.shortcuts import render

from main.forms import ItemForm
from main.models import Item

def show_main(request: HttpRequest) -> HttpResponse:
    items = Item.objects.all()
    
    context = {
        'name': 'Juan Maxwell Tanaya',
        'class': 'C',
        'inventory': items,
    }

    return render(request, "main.html", context)

def add_item(request: HttpRequest) -> HttpResponseRedirect | HttpResponse:
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "add_item.html", context)
