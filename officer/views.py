from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from officer.forms import AdminLoginForm, LoanAmortizationForm
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.admin.views.decorators import staff_member_required
from loans.models import loan_type, loan_application, loan_amortization, loan_payment
from login.models import customer
from officer.forms import (
    AdminUserGroups, CustomerForm, AddUserForm, AdminUpdatePayment, AddLoanType, LoanForm, EditUserForm
)
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def superuser_login_view(request):
    form = AdminLoginForm()
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('loans:homepage'))
    else:
        if request.method == 'POST':
            form = AdminLoginForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    if user.is_staff:
                        login(request, user)
                        return HttpResponseRedirect(reverse('officer:admin-page'))
                    else:
                        return render(request, 'officer/admin_login.html', context={'form': form})
            else:
                return render(request, 'officer/admin_login.html', context={'form': form})
    return render(request, 'officer/admin_login.html', context={'form': form})


@staff_member_required(login_url='/admin-login')
def superuser_logout_view(request):
	logout(request)
	messages.info(request, "You have successfully logged out.")
	return redirect("loans:homepage")



@staff_member_required(login_url='/admin-login')
def adminPage(request):
    count = customer.objects.all().count()
    user_count = User.objects.all().count()
    applications = loan_application.objects.all().count()
    accepted = loan_application.objects.all().filter(loan_status='Accepted').count()
    rejected = loan_application.objects.all().filter(loan_status='Rejected').count()
    pending = loan_application.objects.all().filter(loan_status='Pending').count()
    context= {
        'count':count, 'applications':applications, 'accepted':accepted, 'rejected':rejected, 'pending':pending,
        'user_count':user_count
    }
    return render(request, 'officer/admin_page.html', context)


@staff_member_required(login_url='/admin-login')
def customers(request):
    customers = customer.objects.all()
    context = {'customers':customers}
    return render(request, 'officer/all_customers.html', context)


@staff_member_required(login_url='/admin-login')
def create_customer(request):
    form = CustomerForm()
    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer added.")
            return redirect("officer:admin-page")
        else:
            messages.error(request, "Invalid details.")
    return render(request, 'officer/edit_customer.html', context={'form': form})


@staff_member_required(login_url='/admin-login')
def edit_customer(request, pk):
    cust = customer.objects.get(cust_id=pk)
    form = CustomerForm(instance=cust)
    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES, instance=cust)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer updated.")
            return redirect("officer:admin-page")
        else:
            messages.error(request, "Invalid details.")
    return render(request, 'officer/edit_customer.html', context={'form': form})


@staff_member_required(login_url='/admin-login')
def delete_customer(request, pk):
    cust = customer.objects.get(cust_id=pk)
    if request.method == "POST":
        cust.delete()
        messages.success(request, "Customer deleted.")
        return redirect("officer:admin-page")
    else:
        messages.error(request, "Customer not deleted.")
    return render(request, 'officer/delete_template.html', context={'object': cust})


@staff_member_required(login_url='/admin-login')
def user_group(request):
    form = AdminUserGroups()
    if request.method == 'POST':
        form = AdminUserGroups(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.save()
            messages.info(request, "User group added.")
            return redirect('officer:admin-page')

    return render(request, 'officer/usergroup_form.html', context={'form': form})


@staff_member_required(login_url='/admin-login')
def loans(request):
    loans = loan_application.objects.all()
    context = {'loans':loans}
    return render(request, 'officer/all_loans.html', context)


@staff_member_required(login_url='/admin-login')
def edit_loan(request, pk):
    loan = loan_application.objects.get(application_id=pk)
    form = LoanForm(instance=loan)
    if request.method == "POST":
        form = LoanForm(request.POST, instance=loan)
        if form.is_valid():
            form.save()
            messages.success(request, "Loan updated.")
            return redirect("officer:admin-page")
        else:
            messages.error(request, "Invalid details.")
    return render(request, 'loans/application_form.html', context={'form': form})


@staff_member_required(login_url='/admin-login')
def delete_loan(request, pk):
    loan = loan_application.objects.get(application_id=pk)
    if request.method == "POST":
        loan.delete()
        messages.success(request, "Loan deleted.")
        return redirect("officer:admin-page")
    else:
        messages.error(request, "Loan not deleted.")
    return render(request, 'officer/delete_template.html', context={'object': loan})


@staff_member_required(login_url='/admin-login')
def all_amortizations(request):
    amortizations = loan_amortization.objects.all()
    context = {'amortizations':amortizations}
    return render(request, 'officer/all_amortizations.html', context)


@staff_member_required(login_url='/admin-login')
def create_amortization(request):
    form = LoanAmortizationForm()
    if request.method == "POST":
        form = LoanAmortizationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Loan Amortization added.")
            return redirect("officer:admin-page")
        else:
            messages.error(request, "Invalid details.")
    return render(request, 'loans/amortization_form.html', context={'form': form})


@staff_member_required(login_url='/admin-login')
def edit_amortization(request, pk):
    amor = loan_amortization.objects.get(amortization_id=pk)
    form = LoanAmortizationForm(instance=amor)
    if request.method == "POST":
        form = LoanAmortizationForm(request.POST, instance=amor)
        if form.is_valid():
            form.save()
            messages.success(request, "Loan Amortization updated.")
            return redirect("officer:admin-page")
        else:
            messages.error(request, "Invalid details.")
    return render(request, 'loans/amortization_form.html', context={'form': form})


@staff_member_required(login_url='/admin-login')
def delete_amortization(request, pk):
    amor = loan_amortization.objects.get(amortization_id=pk)
    if request.method == "POST":
        amor.delete()
        messages.success(request, "Loan amortization deleted.")
        return redirect("officer:admin-page")
    else:
        messages.error(request, "Loan amortization not deleted.")
    return render(request, 'officer/delete_template.html', context={'object': amor})


@staff_member_required(login_url='/admin-login')
def create_payment(request):
    form = AdminUpdatePayment()
    if request.method == 'POST':
        form = AdminUpdatePayment(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, "Successful loan payment.") 
            return redirect('officer:admin-page')
        else:
            messages.error(request, "Invalid details.")
    return render(request, 'officer/payment_form.html', context={'form': form})


@staff_member_required(login_url='/admin-login')
def edit_payment(request, pk):
    pay = loan_payment.objects.get(loan_payment_id=pk)
    form = AdminUpdatePayment(instance=pay)
    if request.method == "POST":
        form = AdminUpdatePayment(request.POST, request.FILES, instance=pay)
        if form.is_valid():
            form.save()
            messages.success(request, "Loan payment updated.")
            return redirect("officer:admin-page")
        else:
            messages.error(request, "Invalid details.")
    return render(request, 'officer/payment_form.html', context={'form': form})


@staff_member_required(login_url='/admin-login')
def delete_payment(request, pk):
    pay = loan_payment.objects.get(loan_payment_id=pk)
    if request.method == "POST":
        pay.delete()
        messages.success(request, "Loan payment deleted.")
        return redirect("officer:admin-page")
    else:
        messages.error(request, "Loan amortization not deleted.")
    return render(request, 'officer/delete_template.html', context={'object': pay})


@staff_member_required(login_url='/admin-login')
def all_payments(request):
    pay = loan_payment.objects.all()
    context = {'payments':pay}
    return render(request, 'officer/payments.html', context)


@staff_member_required(login_url='/admin-login')
def users(request):
    user = User.objects.all()
    context = {'user':user}
    return render(request, 'officer/all_users.html', context)


@staff_member_required(login_url='/admin-login')
def add_user(request):
    form = AddUserForm()
    if request.method == "POST":
        form = AddUserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "User added.")
            return redirect("officer:admin-page")
        else:
            messages.error(request, "Invalid details.")
    return render(request, 'officer/add_user.html', context={'form': form})


@staff_member_required(login_url='/admin-login')
def edit_user(request, pk):
    user = User.objects.get(username=pk)
    form = EditUserForm(instance=user)
    if request.method == "POST":
        form = EditUserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "User updated.")
            return redirect("officer:admin-page")
        else:
            messages.error(request, "Invalid details.")
    return render(request, 'officer/add_user.html', context={'form': form})


@staff_member_required(login_url='/admin-login')
def delete_user(request, pk):
    user = User.objects.get(username=pk)
    if request.method == "POST":
        user.delete()
        messages.success(request, "User deleted.")
        return redirect("officer:admin-page")
    else:
        messages.error(request, "User not deleted.")
    return render(request, 'officer/delete_template.html', context={'object': user})


@staff_member_required(login_url='/admin-login')
def loan_types(request):
    types = loan_type.objects.all()
    context = {'types':types}
    return render(request, 'officer/types.html', context)


@staff_member_required(login_url='/admin-login')
def add_loan_type(request):
    form = AddLoanType()
    if request.method == "POST":
        form = AddLoanType(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Loan type added.")
            return redirect("officer:admin-page")
        else:
            messages.error(request, "Invalid details.")
    return render(request, 'officer/loan_type.html', context={'form': form})


@staff_member_required(login_url='/admin-login')
def edit_loan_type(request, pk):
    type = loan_type.objects.get(loan_type_id=pk)
    form = AddLoanType(instance=type)
    if request.method == "POST":
        form = AddLoanType(request.POST, instance=type)
        if form.is_valid():
            form.save()
            messages.success(request, "Loan Type updated.")
            return redirect("officer:admin-page")
        else:
            messages.error(request, "Invalid details.")
    return render(request, 'officer/loan_type.html', context={'form': form})


@staff_member_required(login_url='/admin-login')
def delete_loan_type(request, pk):
    type = loan_type.objects.get(loan_type_id=pk)
    if request.method == "POST":
        type.delete()
        messages.success(request, "Loan Type deleted.")
        return redirect("officer:admin-page")
    else:
        messages.error(request, "Loan Type not deleted.")
    return render(request, 'officer/delete_template.html', context={'object': type})
