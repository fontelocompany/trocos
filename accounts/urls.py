from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', login_required(views.index), name="dash-home"),
    path('account/new', login_required(views.AddAccount), name="add-account"),
    path('account/<int:pk>/edit', login_required(views.EditAccount), name="edit-account"),
    path('account/<int:pk>/delete', login_required(views.DelAccount), name="del-account"), 
]