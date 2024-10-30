from django.urls import path
from .views import about, collection_detail,index,collection_all,new_collection

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('collection/<int:n>', collection_detail, name='collection_detail'),
    path('all/',collection_all,name='collection_all'),
    path('new/', new_collection, name='new_collection'),
]