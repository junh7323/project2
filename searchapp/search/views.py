from django.shortcuts import render
from .models import Card
from django.db.models import Q

# Create your views here.
def searchResult(request):
    
    if 'kw' in request.GET:
        query = request.GET.get('kw')
        products = Card.objects.all().filter(
            Q(name__icontains=query) | #이름 검색
            Q(description__icontains=query) #설명 검색
        )

    return render(request, 'search.html', {'query':query, 'products':products})