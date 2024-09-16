from django.urls import path
from . import views

urlpatterns = [
    # Auth
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('onboarding/', views.onboarding, name='onboarding'),
    path('onboarding/signup', views.signup, name='signup'),


    # Settings
    path('settings/', views.SettingsHome, name="settings"),
    path('settings/user', views.UserSettings, name="user settings"),
    path('settings/family', views.FamilySettings, name="family settings"),
    path('settings/utils', views.UtilSettings, name="utils settings"),
]