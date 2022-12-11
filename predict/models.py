from django.db import models

# Create your models here.

# Gender,Married,Dependents,Education,Self_Employed,
# ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area

class CustomerPredict(models.Model):
    married = (
        (1, 'Yes'),
        (0, 'No')
    )
    dependents = (
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3+')
    )
    education = (
        (0, 'Graduate'),
        (1, 'Not Graduate')
    )
    gender = (
        (1, 'Male'),
        (0, 'Female')
    )
    self = (
        (1, 'Yes'),
        (0, 'No')
    )
    credit = (
        (0.0, '0.0'),
        (1.0, '1.0')
    )
    area = (
        (2, 'Urban'),
        (1, 'Semiurban'),
        (0, 'Rural')
    )
    Gender = models.IntegerField(null=False, blank=False, choices=gender, default="")
    Married = models.IntegerField(choices=married, default="")
    Dependents = models.IntegerField(choices=dependents, default="")
    Education = models.IntegerField(choices=education, default="")
    Self_Employed = models.IntegerField(choices=self, default="")
    ApplicantIncome = models.PositiveIntegerField(default=0)
    CoapplicantIncome = models.PositiveIntegerField(default=0)
    LoanAmount = models.PositiveIntegerField(default=0) 
    Loan_Amount_Term = models.PositiveIntegerField(default=0)
    Credit_History = models.FloatField(default="", choices=credit)
    Property_Area = models.IntegerField(choices=area, default="")

    # def __str__(self):
    #     return self.Property_Area