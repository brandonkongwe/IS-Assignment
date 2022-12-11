from django.contrib import admin
from loans.models import (
    loan_amortization, loan_type, loan_application, 
    loan_payment, sms_log, sms
)
# Register your models here.
admin.site.register(loan_amortization)
admin.site.register(loan_type)
admin.site.register(loan_application)
admin.site.register(loan_payment)
admin.site.register(sms)
admin.site.register(sms_log)