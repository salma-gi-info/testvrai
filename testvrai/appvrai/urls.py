from django.urls import path
from .views import about, collection_detail,index,collection_all

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('collection/<int:n>', collection_detail, name='collection_detail'),
    path('all/',collection_all,name='collection_all'),
]