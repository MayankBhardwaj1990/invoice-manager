from django.urls import path
from . views import *

urlpatterns=[
    path('generate_invoice',generate_invoice,name='generte-invoice'),
    path('generate_invoice_item',generate_invoice_item,name='generte-invoice-itme'),
    path('get_invoices',get_invoices,name='get-invoices'),
    path('get_invoice/<str:pk>',get_invoice,name='get-invoice'),
    path('get_invoice_items/<str:pk>/',get_invoice_items,name='get-invoice_items'),
]