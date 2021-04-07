from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegisterForm, UserInfoForm
from products.models import Product
from .models import Order, User_info
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username= form.cleaned_data.get('username')
			messages.success(request, "Your account has been registered.")
			return redirect('login')			
	else:
		form = UserRegisterForm()
	return render(request, "users/register.html", {"form": form})

@login_required
def profile(request):
	prod = Order.objects.filter(user = request.user.username, order_placed = False)
	print(prod)
	total_bill = 0
	order =list(Order.objects.filter(user= request.user.username, order_placed = False))
	bill = [int(i.item_bill) for i in order ]
	
	context = { "prod": prod, "total_bill": sum(bill) }
	return render(request, 'users/profile.html', context)

@login_required
def quantity(request, pk):
	if request.method == "POST":
		order = Order.objects.filter(prod_id = pk, user = request.user.username, order_placed = False)
		print(order[0].product)
		item_price = int(request.POST['qty']) * order[0].product.price
		print(item_price)
		Order.objects.filter(prod_id = pk, user = request.user.username, order_placed = False).update(quantity = request.POST['qty'], item_bill =item_price)
		messages.success(request, " Quantity of product is saved! ")
	return redirect('profile')
	

@login_required
def UserInfo(request):
	if(request.method=="POST"):
		form = UserInfoForm(request.POST)
		if form.is_valid():
		
			address1 = form.cleaned_data.get('address1')
			address2 = form.cleaned_data.get('address2')
			country = form.cleaned_data.get('country')
			state = form.cleaned_data.get('state')
			pincode = form.cleaned_data.get('pincode')
			phone = form.cleaned_data.get('phone')

			newinfo = User_info(user = request.user, address1 = address1, address2 = address2, country = country, state = state, pincode= pincode, phone = phone )
			newinfo.save()
			Order.objects.filter(user = request.user.username, order_placed = False).update(order_placed = True, shipping_info = newinfo )

			subject = " BuyIt : Order Placed "
			message = " An order has been placed from your account. If it was you click on the link below."
			from_email = settings.EMAIL_HOST_USER
			to_list = [request.user.email]
			send_mail(subject, message, from_email, to_list, fail_silently = True)
			messages.success(request, "Your order has been placed. Check your registered email account for a confirmation mail. Thank you for choosing BuyIt")
			return redirect('home')

	else:
		prod = Order.objects.filter(user = request.user.username, order_placed = False)
		total_bill = 0
		order =list(Order.objects.filter(user= request.user.username, order_placed = False))
		bill = [int(i.item_bill) for i in order ]
		form = UserInfoForm()
		context={
		"form": form,
		"prod":prod,
		"total_bill": sum(bill)
		}
		return render(request, "users/userinfo.html", context)


