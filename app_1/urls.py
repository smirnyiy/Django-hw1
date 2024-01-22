from django.urls import path

from .views import index
from .views import about


urlpatterns = {
    path('', index, name='index'),
    path('about/', about, name='about'),
    
}