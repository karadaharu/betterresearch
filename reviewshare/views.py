from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Paper, Review

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
    doi = request.POST.get('doi', '')
    if doi != '':
        print('save')
        paper = Paper(doi=doi)
        paper.save()
    else:
        print(request.POST)
    return render(request,'reviewshare/create.html')
