from django.db import models
from login.models import customer
from django.contrib.auth.models import User
import uuid

# Create your models here.
class loan_type(models.Model):
    loan_type_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    loan_name = models.CharField(max_length=250)
    description = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.loan_name


class loan_application(models.Model):
    payment_mode = (
        ('Over the Counter', 'Over the Counter'),
        ('Bank Transfer', 'Bank Transfer'), 
        ('Salary Deduction', 'Salary Deduction')
    )
    status = (
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected')
    )
    application_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    control_number = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=False, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_staff': False},
    related_name='customer_loan', null=True, blank=True, default="")
    cust_id = models.ForeignKey(customer, on_delete=models.CASCADE, default="")
    loan_type_id = models.ForeignKey(loan_type, on_delete=models.CASCADE)
    mode_of_payment = models.CharField(max_length=200, choices=payment_mode, default="")
    loan_amount = models.PositiveIntegerField(default=0)
    loan_duration = models.PositiveIntegerField(default=0)
    purpose = models.TextField(null=False, blank=False)
    loan_status = models.CharField(max_length=200, choices=status, default="Pending")
    remarks = models.TextField(null=True, blank=True)
    processed_by = models.ForeignKey(User, limit_choices_to={'is_staff': True}, on_delete=models.CASCADE, 
    null=True, blank=True)

    def __str__(self):
        return self.cust_id.first_name + ' ' + self.cust_id.surname + '' + ', Loan Type: ' + self.loan_type_id.loan_name
    


class loan_amortization(models.Model):
    amortization_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    control_number = models.ForeignKey(loan_application, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_staff': False},
    related_name='customer_amortization', null=True, blank=True, default="")
    date = models.DateTimeField(auto_now_add=True)
    payment_amount = models.PositiveIntegerField(default=0)
    interest_payment = models.PositiveIntegerField(default=0)
    principal_paid = models.PositiveIntegerField(default=0)
    remaining_balance = models.PositiveIntegerField(default=0)

    def __str__(self):
        # return self.control_number.cust_id.user.username
        return self.control_number.cust_id.first_name + ' ' + self.control_number.cust_id.surname + '' + ', Loan Type: ' + self.control_number.loan_type_id.loan_name


class sms(models.Model):
    api_code = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=False, editable=False)
    api_password = models.CharField(max_length=30)
    api_status = models.CharField(max_length=100)
    message = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.api_status


class sms_log(models.Model):
    sms_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    sent_date = models.DateField(auto_now_add=True)
    cust_id = models.ForeignKey(customer, on_delete=models.CASCADE)
    message = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.cust_id.user.username


class loan_payment(models.Model):
    status = (
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected')
    )
    loan_payment_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    payment_reference_number = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=False, editable=False)
    cust_id = models.ForeignKey(customer, on_delete=models.CASCADE, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_staff': False},
    related_name='customer_payment', null=True, blank=True, default="")
    date = models.DateField(auto_now_add=True)
    payment_amount = models.PositiveIntegerField(default=0)
    proof_of_payment = models.FileField(upload_to='docs')
    payment_status = models.CharField(max_length=200, choices=status, default="Pending")
    comments = models.TextField(null=True, blank=True)
    reviewed_by = models.ForeignKey(User, limit_choices_to={'is_staff': True}, on_delete=models.CASCADE, 
    null=True, blank=True)

    def __str__(self):
        return self.cust_id.first_name + ' ' + self.cust_id.surname
