from django.db import models

# Create your models here.
class Invoice(models.Model):
    exhibition_name = models.CharField(max_length=100)
    date = models.DateField()
    customer_name = models.CharField(max_length=100)
    customer_mobile = models.CharField(max_length=50)
    customer_email = models.EmailField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Invoice {self.id} - {self.customer_name}"
    
class LineItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='line_items')
    vendor_name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    code = models.CharField(max_length=50, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.description} - {self.price}"