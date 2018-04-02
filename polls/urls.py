from django.urls import path

from . import views

#Path har argumenten URLPath och sen viewfunktionen som man kan namege med name= for att kunna hitta senare.
urlpatterns = [
    path('', views.index, name='index'),
]
