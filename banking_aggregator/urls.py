from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('loans/', include('apps.loans.urls')),
    path('banks/', include('apps.banks.urls')),
    path('users/', include('apps.users.urls')),
]