from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('get-local-ip', views.get_local_ip, name='get-local-ip')
]
