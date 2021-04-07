from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.models import User
from users.models import Order
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

def home(request):
	if request.method =='POST':
		category = request.POST['category']
		print(category)
		prod = Product.objects.filter(category__contains = category) | Product.objects.filter(name__contains = category) | Product.objects.filter(model__contains = category)
		order =list(Order.objects.filter(user= request.user.username, order_placed = False))
		ordered_prod = [i.product for i in order]
		

		page = request.GET.get('page', 1)
		paginator = Paginator(prod, 5)
		try:
			prod = paginator.page(page)	
		except PageNotAnInteger:
			prod = paginator.page(1)
		except EmptyPage:
			prod = paginator.page(paginator.num_pages)	
		content = { "prod": prod , "order": ordered_prod}
		return render(request, "products/home.html", content )	    	        		    		        	        

	else:	
		prod = Product.objects.all()
		order =list(Order.objects.filter(user= request.user.username, order_placed = False))
		ordered_prod = [i.product for i in order]
		print("X: ",ordered_prod)

		page = request.GET.get('page', 1)
		paginator = Paginator(prod, 5)
		try:
			prod = paginator.page(page)	
		except PageNotAnInteger:
			prod = paginator.page(1)
		except EmptyPage:
			prod = paginator.page(paginator.num_pages)	

		content = { "prod": prod , "order": ordered_prod}
		return render(request, "products/home.html", content)

def product_detail(request, pk):
	order =list(Order.objects.filter(user= request.user.username, order_placed = False))
	ordered_prod = [i.product for i in order]
	prod = Product.objects.filter(id=pk)
	return render(request, "products/product_detail.html", {"prod":prod[0] , "order": ordered_prod})


@login_required
def add_product(request, pk):
	if request.method == 'POST':
		prod_added = Product.objects.filter(id=pk)[0]
		print(prod_added)
		if Order.objects.filter(user = request.user.username, prod_id = prod_added.id, product= prod_added, order_placed = False ).exists():			
			Order.objects.filter(user = request.user.username, prod_id = prod_added.id,  product= prod_added, order_placed = False  ).delete()
			messages.error(request, "Product removed from cart.")			
		else:		
			p = Order(user = request.user.username , prod_id = prod_added.id,  product= prod_added, item_bill = int(prod_added.price) )
			messages.success(request, "Product added to your cart. ")
			print(p)
			p.save()
		return redirect('home')
	else:
		return redirect('home')

