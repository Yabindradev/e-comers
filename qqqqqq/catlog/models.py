
from django.db import models
from django.contrib.auth.models import User
from .city import YOUR_CITY, YOUR_PROVINCE
from phone_field import PhoneField
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=120)  # max_length = required
    product_code_number = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    is_public = models.BooleanField(default=True)
    is_discountable = models.BooleanField(default=True)
    first_images = models.ImageField()
    second_images = models.ImageField(blank=True, null=True)
    third_images = models.ImageField(blank=True, null=True)
    forth_images = models.ImageField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)
    price = models.BigIntegerField()
    is_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Customer(models.Model):
    YOUR_TITL = [
        ('MR', 'Mr'),
        ('MISS', 'Miss'),
        ('MRS', 'Mrs'),
        ('MS', 'Ms'),
        ('DR', 'Dr'),
    ]
    title = models.CharField(max_length=20, choices=YOUR_TITL)
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    first_line_of_address = models.CharField(max_length=255, blank=False, null=False)
    second_line_of_address = models.CharField(max_length=255, blank=True, null=True)
    third_line_of_address = models.CharField(max_length=255, blank=True, null=True)
    Province = models.CharField(max_length=30, choices=YOUR_PROVINCE)
    city = models.CharField(max_length=30, choices=YOUR_CITY)
    Post_Zip_code = models.BigIntegerField(blank=True, null=True)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    instructions = models.TextField( blank=True, null=True)
    
    
    
    def __str__(self):
        return self.first_name
