from django.urls import path
from . import views

urlpatterns = [
    path('data/', views.index, name="index"),
    path('data/inflation', views.inflation, name='inflation page'),
    path('data/fx', views.fx, name='fx page')
]