# Generated by Django 4.1.2 on 2022-11-05 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("predict", "0016_alter_customerpredict_credit_history_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="customerpredict",
            old_name="Applicant_Income",
            new_name="ApplicantIncome",
        ),
        migrations.RenameField(
            model_name="customerpredict",
            old_name="Coapplicant_Income",
            new_name="CoapplicantIncome",
        ),
        migrations.RenameField(
            model_name="customerpredict", old_name="Loan_Amount", new_name="LoanAmount",
        ),
    ]