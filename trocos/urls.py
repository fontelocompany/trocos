import debug_toolbar

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # Authentication/Onboarding
    path('', include('users.urls')), 

    # Dasboard
    path('dash/', include('accounts.urls')),
    path('dash/budget/', include('budget.urls')),
    path('dash/investments/', include('investments.urls')),
    path('dash/property/', include('property.urls')),
    path('dash/transactions/', include('transactions.urls')),

    path('admin', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
]
