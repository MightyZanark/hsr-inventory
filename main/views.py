from datetime import datetime

from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from django.core import serializers
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Sum
from django.views.decorators.csrf import csrf_exempt

from main.forms import ItemForm, RegisterForm
from main.models import Item


@login_required(login_url="/login")
def show_main(request: HttpRequest) -> HttpResponse:
    items = Item.objects.order_by("-amount").filter(user=request.user)
    total_amt = 0
    if len(items) != 0:
        total_amt = items.aggregate(Sum("amount"))["amount__sum"]

    context = {
        "name": request.user.username,
        "class": "C",
        "inventory": items,
        "item_amt": len(items),
        "total_amt": total_amt,
        "last_login": request.COOKIES["last_login"],
    }

    return render(request, "main.html", context)


def add_item(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        # form.save()
        item: Item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse("main:show_main"))

    context = {"form": form}
    return render(request, "add_item.html", context)


@csrf_exempt
def add_item_ajax(request: HttpRequest) -> HttpResponse | HttpResponseNotFound:
    if request.method == "POST":
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        category = request.POST.get("category")
        user = request.user

        new_item = Item(name=name, amount=amount, description=description, category=category, user=user)
        new_item.save()

        return HttpResponse(b"Successfully added item!", status=201)
    
    return HttpResponseNotFound()


def delete_item(request: HttpRequest, id: int) -> HttpResponseRedirect:
    item = Item.objects.get(pk=id)
    item.delete()
    return HttpResponseRedirect(reverse("main:show_main"))


def add_subtract_item_by_one(request: HttpRequest, id: int, option: int) -> HttpResponseRedirect:
    item = Item.objects.get(pk=id)
    if option == 1:
        item.amount += 1
    elif option == 0:
        if item.amount > 0:
            item.amount -= 1
    item.save()
    return HttpResponseRedirect(reverse("main:show_main"))


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


def get_item_json(request: HttpRequest) -> HttpResponse:
    items = Item.objects.filter(user=request.user).order_by("-amount")
    return HttpResponse(serializers.serialize("json", items))


def register_user(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Successfully created your account!"
            )
            return redirect("main:login")
    
    context = {"form": form}
    return render(request, "register.html", context)


def login_user(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            resp = HttpResponseRedirect(reverse("main:show_main"))
            resp.set_cookie("last_login", str(datetime.now()))
            return resp
        
        else:
            messages.info(
                request,
                "Incorrect username or password. Please try again."
            )
    
    context = {}
    return render(request, "login.html", context)


def logout_user(request: HttpRequest) -> HttpResponseRedirect:
    logout(request)
    resp = HttpResponseRedirect(reverse("main:login"))
    resp.delete_cookie("last_login")
    return resp
