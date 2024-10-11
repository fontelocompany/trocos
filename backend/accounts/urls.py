from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', login_required(views.index), name="dash-home"),
    path('accounts', login_required(views.AccountsHome), name="accounts-home"),
    path('account/new', login_required(views.AddAccount), name="add-account"),
    path('account/<int:pk>', login_required(views.EditAccount), name="detail-account"),
    path('account/<int:pk>/edit', login_required(views.EditAccount), name="edit-account"),
    path('account/<int:pk>/delete', login_required(views.DelAccount), name="del-account"), 
]