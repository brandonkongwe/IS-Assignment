from django.db import models
from django.contrib.auth.models import User, Group
import uuid

# Create your models here.
class user_group(Group):
    group_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    # group_name = models.CharField(max_length=250, null=False, blank=False)
    description = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.name


class customer(models.Model):
    account_status = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive')
    )
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE, limit_choices_to={'is_staff': False},
    related_name='customer', default="user=request.user.username")
    cust_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    first_name = models.CharField(max_length=250, null=False, blank=False)
    surname = models.CharField(max_length=250, null=False, blank=False)
    complete_address = models.CharField(max_length=250)
    contact_number = models.IntegerField(null=False, blank=False)
    email_address = models.EmailField(max_length=100, null=False, blank=False, default="")
    gender =  models.CharField(max_length=30, null=False, blank=False, default="")
    civil_status = models.CharField(max_length=250, null=False, blank=False)
    birthdate = models.DateField()
    age = models.IntegerField(null=False, blank=False)
    profile_pic = models.ImageField(upload_to='img', null=True, blank=True)
    # username = models.CharField(max_length=250, null=False, blank=False)
    # username = models.OneToOneField(user, unique=True, limit_choices_to={'is_staff': False},on_delete=models.CASCADE, 
    # related_name="customer")
    # password = models.CharField(max_length=30)
    account_status = models.CharField(max_length=100, choices=account_status, default="")

    def __str__(self):
        return self.user.username
