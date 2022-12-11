from django import forms
from django.forms import ModelForm
from predict.models import CustomerPredict


class PredictForm(ModelForm):
    class Meta:
        model = CustomerPredict
        fields = "__all__"
        labels = {
            'ApplicantIncome': 'Applicant Income',
            'CoapplicantIncome': 'Coapplicant Income',
            'LoanAmount': 'Loan Amount'
        }
