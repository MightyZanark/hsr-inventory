from django.urls import path
from main.views import show_main, add_item

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add-item', add_item, name='add_item')
]
