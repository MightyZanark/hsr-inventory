from django.urls import path
from main.views import show_main, add_item, \
                        show_xml, show_xml_by_id, \
                        show_json, show_json_by_id

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add-item', add_item, name='add_item'),
    path('xml/', show_xml, name='show_xml'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/', show_json, name='show_json'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id')
]
