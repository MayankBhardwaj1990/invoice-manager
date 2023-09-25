from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from uuid import UUID
from . serializers import *
from . models import *

@api_view(['POST'])
def generate_invoice(request):
    serializer=InvoiceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    else:
        return Response({"error": "Invalid data"},status = status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def generate_invoice_item(request):
    serializer=InvoiceItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    else:
        return Response({"error":"invalid data"},status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def get_invoice(request,pk):
    invoice=Invoice.objects.get(id=pk)
    invoice_serializer=InvoiceSerializer(invoice)
    items = InvoiceItem.objects.filter(invoice_id=pk)
    item_serializer = InvoiceItemSerializer(items, many=True)
    invoice_data = invoice_serializer.data
    invoice_data['items'] = item_serializer.data

    return Response(invoice_data, status=status.HTTP_200_OK)

    
@api_view(['GET'])
def get_invoices(request):
    invoices=Invoice.objects.all()
    serializer=InvoiceSerializer(invoices,many=True)
    for invoice in serializer.data:
        invoice_id = invoice['id']
        items = InvoiceItem.objects.filter(invoice_id=invoice_id)
        item_serializer = InvoiceItemSerializer(items, many=True)
        invoice['items'] = item_serializer.data

    return Response(serializer.data, status=status.HTTP_200_OK)

    
@api_view(['GET'])
def get_invoice_items(request, pk):
    invoice_items=InvoiceItem.objects.filter(invoice=pk)
    serializer=InvoiceItemSerializer(invoice_items,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)