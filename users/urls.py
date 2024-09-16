from django.urls import path
from . import views

urlpatterns = [
    # Auth
    path('login/', views.login, name='login'),
    path('onboarding/', views.onboarding, name='onboarding'),


    # Settings
    path('settings/', views.SettingsHome, name="settings"),
    path('settings/user', views.UserSettings, name="user settings"),
    path('settings/family', views.FamilySettings, name="family settings"),
    path('settings/utils', views.UtilSettings, name="utils settings"),
]