from django.urls import path
from .views import InvoiceListCreateAPIView, InvoiceRetrieveAPIView

urlpatterns = [
    path('invoices/', InvoiceListCreateAPIView.as_view(), name='invoice-list-create'),
    path('invoices/<int:pk>/', InvoiceRetrieveAPIView.as_view(), name='invoice-retrieve'),
]
