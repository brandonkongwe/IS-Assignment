# Generated by Django 4.1.2 on 2022-10-19 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("loans", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="loan_application",
            name="loan_status",
            field=models.CharField(
                choices=[
                    ("Pending", "Pending"),
                    ("Accepted", "Accepted"),
                    ("Rejected", "Rejected"),
                ],
                default="Pending",
                max_length=200,
            ),
        ),
        migrations.AlterField(
            model_name="loan_payment",
            name="payment_status",
            field=models.CharField(
                choices=[
                    ("Pending", "Pending"),
                    ("Accepted", "Accepted"),
                    ("Rejected", "Rejected"),
                ],
                default="Pending",
                max_length=200,
            ),
        ),
    ]