from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from . import utils
from . import services

# Create your views here.
@require_http_methods(['GET'])
def index(request):
    context = {}
    return render(request, 'app/index.html', context)

@require_http_methods(['GET'])
def get_local_ip(request):
    ip = utils.get_local_ip()
    print(f'local ip: {ip}')
    return HttpResponse(str(ip))

@require_http_methods(['POST'])
def debug_button_1(request):
    return None

@require_http_methods(['GET'])
def available_services(request):
    discovered = services.service.get_discovered_services()
    services.service.scan()
    return HttpResponse(str(discovered))