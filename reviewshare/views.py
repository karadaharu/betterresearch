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
    doi = request.GET.get('doi', '')
    print('doi is')
    print(doi)
    paper = Paper(doi=doi)
    rev = Review(paper=paper)
    print(rev.url)
    review_filter = Review.objects.filter(paper=paper)
    if review_filter.exists():
        reviews = review_filter
    else:
        reviews = None
    print(reviews)
    return render(request,'reviewshare/search.html', {
        'doi' : request.GET.get('doi', ''),
        'reviews' : reviews
    })

def new(request):
    return render(request,'reviewshare/new.html', {
        'doi' : request.GET.get('doi', ''),
    })

def create(request):
    doi = request.POST.get('doi', '')
    url = request.POST.get('url', '')
    if doi != '' and url != '':
        print('save')
        print(url)
        paper = Paper(doi=doi)
        paper.save()
        review = Review(paper=paper, url=url)
        review.save()
    else:
        print(request.POST)
    return render(request,'reviewshare/create.html')
