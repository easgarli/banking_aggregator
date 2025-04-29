from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('loans/', include('banking_aggregator.apps.loans.urls')),
    path('banks/', include('banking_aggregator.apps.banks.urls')),
    path('users/', include('banking_aggregator.apps.users.urls')),
    path('users/', include('django.contrib.auth.urls')),  # Include built-in auth URLs
    path('', include('banking_aggregator.apps.core.urls')),  # Use core app for the root path
]
