from rest_framework import generics
from .models import Invoice
from .serializers import InvoiceSerializer

class InvoiceListCreateAPIView(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class InvoiceRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
