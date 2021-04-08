from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from django_countries.fields import CountryField
from phone_field import PhoneField

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	cart = models.ManyToManyField(Product, related_name = "ProductsAdded", blank=True)

	def __str__(self):
		return f'{self.user.username} Profile '

class User_info(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	address1 = models.CharField(default="", max_length=250)
	address2 = models.CharField(default="", max_length=250)
	country =models.CharField(default="", max_length=50)
	state = models.CharField(default="", max_length=50)
	pincode = models.CharField(default="", max_length=10)
	phone = PhoneField(blank=True, help_text='Contact phone number')
	order_placed_on = models.DateField(blank = True, null=True)
	

	def __str__(self):
		return f'{self.id} {self.user.username} on {self.order_placed_on}'
    	
    

    
		



class Order(models.Model):
	user = models.CharField(max_length= 100, default ="")
	prod_id = models.CharField(max_length= 100, default ="")
	quantity = models.IntegerField(default=1)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	item_bill = models.IntegerField(default=0)
	order_placed = models.BooleanField(default = False)
	shipping_info = models.ForeignKey(User_info, on_delete=models.CASCADE, blank=True, null= True)
	order_placed_on = models.DateField(blank = True, null =True)

	def __str__(self):
		return f'{self.user} - {self.product} on {self.order_placed_on} '






