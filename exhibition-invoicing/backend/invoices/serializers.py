from rest_framework import serializers
from .models import Invoice, LineItem

class LineItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineItem
        fields = ['id', 'vendor_name', 'description', 'code', 'price']

class InvoiceSerializer(serializers.ModelSerializer):
    line_items = LineItemSerializer(many=True)

    class Meta:
        model = Invoice
        fields = [
            'id', 'exhibition_name', 'date',
            'customer_name', 'customer_mobile', 'customer_email',
            'total_price', 'line_items'
        ]

    def create(self, validated_data):
        line_items_data = validated_data.pop('line_items')
        invoice = Invoice.objects.create(**validated_data)

        # Calculate total price
        total = 0
        for item_data in line_items_data:
            line_item = LineItem.objects.create(invoice=invoice, **item_data)
            total += float(line_item.price)

        # Update the invoice total_price
        invoice.total_price = total
        invoice.save()
        return invoice
