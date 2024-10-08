from django.forms import ModelForm
from main.models import ProductEntry
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = ProductEntry
        fields = ["Product_Name", "Product_Description", "Product_Price"]

    def clean_product_name(self):
        product_name = self.cleaned_data["product_name"]
        return strip_tags(product_name)

    def clean_product_description(self):
        product_description = self.cleaned_data["product_description"]
        return strip_tags(product_description)