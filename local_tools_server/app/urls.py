from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('get-local-ip', views.get_local_ip, name='get-local-ip'),
    path('available-services', views.available_services, name='available-services'),
    path('debug-button-1', views.debug_button_1, name='debug-button-1'),
]
