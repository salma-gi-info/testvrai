from django.shortcuts import get_object_or_404, redirect, render
from .models import Collec
from .forms import CollecForm
from django.utils import timezone

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


def new_collection(request):
    if request.method == "POST":
        form = CollecForm(request.POST)
        if form.is_valid():
            collection = form.save(commit=False)
            collection. creation_date= timezone.now()  
            collection.save()
            return redirect('collection_detail', n=collection.id) 
    else:
        form = CollecForm()
    return render(request, 'new_collection.html', {'form': form})


def delete_collection(request, id):
    collection = get_object_or_404(Collec, id=id)
    if request.method == 'POST':
        collection.delete()
        return redirect('collection_all')  
    return render(request, 'delete_collection.html', {'collection': collection})
