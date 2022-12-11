from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from django.forms import ModelForm
from loans.models import loan_amortization, loan_application, loan_payment, loan_type
from login.models import user_group, customer


class AdminLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class AdminUpdatePayment(forms.ModelForm):
    class Meta:
        model = loan_payment
        fields = '__all__'
        labels = {
            'cust_id': 'Customer ID',
            'user': 'Username',
        }


class AdminUserGroups(ModelForm):
    class Meta:
        model = user_group
        fields = '__all__'


class CustomerForm(ModelForm):
    class Meta:
        model = customer
        exclude = ['password']
        labels = {
            'user': 'Username',
        }


class AddUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name','username', 'email', 'is_staff', 'password1', 'password2')


class EditUserForm(UserChangeForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name','username', 'email', 'is_staff')


class AddLoanType(ModelForm):
    class Meta:
        model = loan_type
        fields = '__all__'


class LoanForm(ModelForm):
    class Meta:
        model = loan_application
        fields = '__all__'


class LoanAmortizationForm(ModelForm):
    class Meta:
        model = loan_amortization
        fields = '__all__'
        labels = {
            'user': 'Username',
        }
