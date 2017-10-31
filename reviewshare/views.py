from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('reviewshare/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def search(request):
    template = loader.get_template('reviewshare/search.html')
    context = {}
    print(request.GET.get('doi', 'default'));
    return HttpResponse(template.render(context, request))
