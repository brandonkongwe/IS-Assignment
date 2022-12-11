from django import forms
from django.forms import ModelForm
from loans.models import loan_application, loan_payment



# Create your forms here.
class LoanApplicationForm(ModelForm):
    class Meta:
        model = loan_application
        exclude = ['loan_status', 'remarks', 'processed_by']
        labels = {
            'cust_id': 'Customer ID',
            'loan_type_id': 'Loan Type',
            'user': 'Username',
        }


class CustomerUpdatePayment(ModelForm):
    class Meta:
        model = loan_payment
        exclude = ['payment_status', 'comments', 'reviewed_by']
        labels = {
            'cust_id': 'Customer ID',
            'user': 'Username',
        }