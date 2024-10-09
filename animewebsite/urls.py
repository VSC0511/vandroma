from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('romance/', views.romance, name='romance'),
    path('isekai/', views.isekai, name='isekai'),
    path('shounen/', views.shounen, name='shounen'),
    path('comedy/', views.comedy, name='comedy'),
    path('fantasy/', views.fantasy, name='fantasy'),
]
