from django.shortcuts import render
from store.models import *
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
@staff_member_required
def admin(request):
	context = {'user':0}
	return render(request, 'adminpage/admin.html', context)

@staff_member_required
def categories(request):
	if(request.POST.get('id')):
		cateid = request.POST.get('id')
		name = request.POST.get('name')

		cate = Category.objects.get(id=cateid)
		if(len(Name)>0):
			cate.Name = name
		cate.save()
		context = {'cate':cate}
		return render(request, 'adminpage/category-view.html', context)
	if(request.GET.get('id')):
		cateid = request.GET.get('id')
		cate = Category.objects.get(id=cateid)
		if(request.GET.get('action')=="edit"):
			context = {'cate':cate}
			return render(request, 'adminpage/category-view.html', context)
		if(request.GET.get('action')=="delete"):
			cate.delete()
	categories = Category.objects.all()
	context = {'categories':categories}
	return render(request, 'adminpage/categories.html', context)

@staff_member_required
def users(request):
	if(request.POST.get('id')):
		userid = request.POST.get('id')
		username = request.POST.get('username')
		email = request.POST.get('email')
		password = request.POST.get('password')

		user = User.objects.get(id=userid)
		if(len(password)>0):
			user.set_password(password)
			user.save()
		if(len(username)>0):
			user.email = email
		if(len(email)>0):
			user.username = username
		user.save()
		context = {'user':user}
		return render(request, 'adminpage/user-view.html', context)
	if(request.GET.get('id')):
		userid = request.GET.get('id')
		user = User.objects.get(id=userid)
		if(request.GET.get('action')=="edit"):
			context = {'user':user}
			return render(request, 'adminpage/user-view.html', context)
		if(request.GET.get('action')=="delete"):
			user.delete()
	users = User.objects.all()
	context = {'users':users}
	return render(request, 'adminpage/users.html', context)

@staff_member_required
def products(request):
	products = Product.objects.all()
	context = {'products':products}
	return render(request, 'adminpage/products.html', context)

@staff_member_required
def orders(request):
	orders = Order.objects.all()
	context = {'orders':orders}
	return render(request, 'adminpage/orders.html', context)