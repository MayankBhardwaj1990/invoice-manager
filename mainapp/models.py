import uuid
from django.db import models

class Invoice(models.Model):
        id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
        date=models.DateTimeField(auto_now_add=True)

        def __str__(self):
                return str(self.id)
        
class InvoiceItem(models.Model):
        id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
        invoice=models.ForeignKey(Invoice,related_name='items',on_delete=models.CASCADE)
        units=models.IntegerField(null=True,blank=True)
        description=models.CharField(max_length=100,null=True,blank=True)
        amount=models.DecimalField(null=True,blank=True,max_digits=10,decimal_places=2)

        def __str__(self):
                return self.description        