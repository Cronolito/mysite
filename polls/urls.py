from django.urls import path

from . import views

#Path har argumenten URLPath och sen viewfunktionen som man kan namege med name= for att kunna hitta senare.
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
