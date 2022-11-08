from django.forms import ModelForm
from .models import *


class ProductsFrom(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        # exclude =['fields_name'] #for remove not needed fields
        
        
class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class CustomerForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        