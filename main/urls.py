from django.urls import path
from main.views import show_main, add_item, delete_item, add_subtract_item_by_one, \
                        show_xml, show_xml_by_id, \
                        show_json, show_json_by_id, \
                        get_item_json, add_item_ajax, delete_item_ajax, \
                        register_user, login_user, logout_user, \
                        add_item_flutter, get_item_flutter

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add-item', add_item, name='add_item'),
    path('create-ajax', add_item_ajax, name='create_ajax'),
    path('delete-item/<int:id>/', delete_item, name='delete_item'),
    path('delete-ajax/<int:id>/', delete_item_ajax, name='delete_ajax'),
    path('add-subtract-item-amount/<int:id>/<int:option>', add_subtract_item_by_one, name='add_subtract_item_by_one'),
    path('xml/', show_xml, name='show_xml'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/', show_json, name='show_json'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('get-item/', get_item_json, name='get_item_json'),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('add-flutter/', add_item_flutter, name='add_flutter'),
    path('get-item-flutter/', get_item_flutter, name='get_item_flutter'),
]
