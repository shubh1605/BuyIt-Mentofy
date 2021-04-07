from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django_countries.fields import CountryField
from phone_field import PhoneField
from .models import User_info

class UserRegisterForm(UserCreationForm):
	
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ['first_name','last_name','username','email','password1','password2']


class UserInfoForm(forms.Form):
	address1 = forms.CharField(widget = forms.TextInput(attrs ={ 'placeholder': "1/101, Harikrishna building, MG Road" }))
	address2 = forms.CharField(widget = forms.TextInput(attrs ={ 'placeholder': "Mulund west, Mumbai" }))
	country = CountryField(blank_label ='(Select your country)').formfield()
	state = forms.CharField(widget = forms.TextInput(attrs ={ 'placeholder': "State" }))
	pincode = forms.CharField(widget = forms.TextInput(attrs ={ 'placeholder': "Pincode" }))
	phone = PhoneField(blank=True, help_text='Contact phone number').formfield()
    		

	class Meta:
		model = User_info
		fields = ['address1', 'address2', 'country', 'state', 'pincode', 'phone']
