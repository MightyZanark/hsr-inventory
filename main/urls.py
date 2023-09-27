from django.urls import path
from main.views import show_main, add_item, delete_item, add_subtract_item_by_one, \
                        show_xml, show_xml_by_id, \
                        show_json, show_json_by_id, \
                        register_user, login_user, logout_user

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add-item', add_item, name='add_item'),
    path('delete-item/<int:id>/', delete_item, name='delete_item'),
    path('add-subtract-item-amount/<int:id>/<int:option>', add_subtract_item_by_one, name='add_subtract_item_by_one'),
    path('xml/', show_xml, name='show_xml'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/', show_json, name='show_json'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
