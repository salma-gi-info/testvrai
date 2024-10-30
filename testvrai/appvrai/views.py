from django.shortcuts import get_object_or_404, render

from .models import Collec

# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')
def collection_detail(request, n):
    collection = get_object_or_404(Collec, id=n)
    return render(request, 'collection_detail.html', {'collection': collection})

def collection_all(request):
    collections=Collec.objects.all()
    return render(request,'collection_all.html',{'collections':collections})