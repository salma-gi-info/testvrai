from django.urls import path
from .views import about, collection_detail, index

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
     path('collection/<int:n>', collection_detail, name='collection_detail'),
]