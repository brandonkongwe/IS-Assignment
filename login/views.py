from django.shortcuts import render, redirect
from login.forms import CustomerSignupForm, CustomerLoginForm
from login.models import customer
from django.contrib.auth.models import User
from officer.forms import CustomerForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def sign_up_view(request):
	form = CustomerSignupForm()
	if request.method == "POST":
		form = CustomerSignupForm(request.POST, request.FILES)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful. Enter your details below." )
			return redirect("login:customer-details")
		else:	
			messages.error(request, "Unsuccessful registration. Invalid information.")
	return render (request, "login/register.html", context={"form":form})


@login_required(login_url='/customer-login')
def customer_details(request):
	customers = customer.objects.all().filter(user=request.user.id)
	form = CustomerForm()
	form.fields['user'].queryset = User.objects.filter(username=request.user.username)
	if request.method == "POST":
		form = CustomerForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, "Details added successfully.")
			return redirect("loans:user-page")
		else:
			messages.error(request, "Invalid information, try again.")
	return render(request, "login/customer_details.html", context={"form":form, "customers":customers})


@login_required(login_url='/customer-login')
def edit_details(request, pk):
    cust = customer.objects.get(cust_id=pk)
    form = CustomerForm(instance=cust)
    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES, instance=cust)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer updated.")
            return redirect("loans:user-page")
        else:
            messages.error(request, "Invalid details.")
    return render(request, 'login/customer_details.html', context={'form': form})


def login_view(request):
	if request.method == "POST":
		form = CustomerLoginForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("loans:user-page")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = CustomerLoginForm()
	return render(request, "login/login.html", context={"form":form})


@login_required()
def logout_view(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("loans:homepage")
