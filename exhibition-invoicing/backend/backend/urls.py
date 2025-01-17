from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('invoices.urls')),  # route everything under /api/ to our invoices app
]
