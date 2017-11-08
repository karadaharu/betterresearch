from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('reviewshare/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def search(request):
    print(request.GET.get('doi', 'default'));
    return render(request,'reviewshare/search.html', {
        'doi' : request.GET.get('doi', ''),
    })

def new(request):
    return render(request,'reviewshare/new.html', {
        'doi' : request.GET.get('doi', ''),
    })

def create(request):
    return render(request,'reviewshare/create.html')

