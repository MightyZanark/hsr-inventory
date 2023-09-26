from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from main.models import Item


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "amount", "description", "category"]

# Unused for the time being
class RegisterForm(UserCreationForm):
    CLASS_CHOICES = [
        ("A", "PBP A"),
        ("B", "PBP B"),
        ("C", "PBP C"),
        ("D", "PBP D"),
        ("E", "PBP E"),
        ("F", "PBP F"),
    ]
    pbp_class = forms.ChoiceField(choices=CLASS_CHOICES)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ("pbp_class",)
