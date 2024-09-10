from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template('app/index.html')
    context = {}
    return render(request, 'app/index.html', context)

def get_local_ip(request):
    return HttpResponse('localhost')
 