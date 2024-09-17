from django.forms import ModelForm
from main.models import ProductEntry

class ProductForm(ModelForm):
    class Meta:
        model = ProductEntry
        fields = ["Product_Name", "Product_Description", "Product_Price"]