from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="property-home"),
    
    # Car
    path('car/new', views.SaveCar, name="add-car"),
    path('car/<int:pk>/edit', views.EditCar, name="edit-car"),
    path('car/<int:pk>/delete', views.DelCar, name="del-car"),
    
    # Residency
    path('residency/new', views.SaveResidency, name="add-residency"),
    path('residency/<int:pk>/edit', views.EditResidency, name="edit-residency"),
    path('residency/<int:pk>/delete', views.DelResidency, name="del-residency"),

]