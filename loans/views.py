from django.shortcuts import render, redirect
from loans.forms import LoanApplicationForm, CustomerUpdatePayment
from loans.models import loan_amortization, loan_application, loan_payment, loan_type
from login.models import customer
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

# Create your views here.
def homepage(request):
    count = customer.objects.all().count()
    context = {'count':count}
    return render(request, 'loans/home.html', context)


@login_required(login_url='/customer-login')
def loans(request):
    customers = customer.objects.all().filter(user=request.user.id)
    loans = loan_application.objects.all().filter(user=request.user.id)
    context = {'loans':loans, 'customers':customers}
    return render(request, 'loans/applications.html', context)


@login_required(login_url='/customer-login')
def create_loan(request):
    customers = customer.objects.all().filter(user=request.user.id)
    form = LoanApplicationForm()
    form.fields['user'].queryset = User.objects.filter(username=request.user.username)
    form.fields['cust_id'].queryset = customer.objects.filter(user=request.user.id)
    if request.method == 'POST':
        form = LoanApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Successful loan application.")
            return redirect('loans:user-page')
    return render(request, "loans/application_form.html", context={"form":form, 'customers':customers})


@login_required(login_url='/customer-login')
def amortizations(request):
    customers = customer.objects.all().filter(user=request.user.id)
    amortizations = loan_amortization.objects.all().filter(user=request.user.id)
    context = {'amortizations':amortizations, 'customers':customers}
    return render(request, 'loans/amortizations.html', context)


@login_required(login_url='/customer-login')
def loan_types(request):
    customers = customer.objects.all().filter(user=request.user.id)
    types = loan_type.objects.all()
    context = {'types':types, 'customers':customers}
    return render(request, 'officer/types.html', context)


@login_required(login_url='/customer-login')
def all_payments(request):
    customers = customer.objects.all().filter(user=request.user.id)
    pay = loan_payment.objects.all().filter(user=request.user.id)
    context = {'payments':pay, 'customers':customers}
    return render(request, 'loans/all_payments.html', context)


@login_required(login_url='/customer-login')
def loanPayment(request):
    customers = customer.objects.all().filter(user=request.user.id)
    form = CustomerUpdatePayment()
    form.fields['user'].queryset = User.objects.filter(username=request.user.username)
    form.fields['cust_id'].queryset = customer.objects.filter(user=request.user.id)
    if request.method == 'POST':
        form = CustomerUpdatePayment(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, "Successful loan payment.")
            return redirect('loans:user-page')
        else:
            messages.error(request, "Invalid details.")
    return render(request, 'loans/user_payment.html', context={'form': form, 'customers':customers})


@login_required(login_url='/customer-login')
def userPage(request):
    customers = customer.objects.all().filter(user=request.user.id)
    loan_count = loan_application.objects.filter(user=request.user.id).count()
    accepted = loan_application.objects.all().filter(user=request.user.id).filter(loan_status='Accepted').count()
    rejected = loan_application.objects.all().filter(user=request.user.id).filter(loan_status='Rejected').count()
    pending = loan_application.objects.all().filter(user=request.user.id).filter(loan_status='Pending').count()
    remaining = loan_amortization.objects.all().filter(user=request.user.id).aggregate(Sum('remaining_balance'))['remaining_balance__sum']
    context = {'loan_count':loan_count, 'accepted':accepted, 'rejected':rejected, 'pending':pending,
    'customers':customers, 'remaining':remaining
    }
    return render(request, 'loans/user_page.html', context)
