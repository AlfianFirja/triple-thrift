import uuid
from django.db import models

class ProductEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Product_Name = models.CharField(max_length=255)
    Product_Description = models.TextField()
    Product_Price = models.IntegerField()
