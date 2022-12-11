from django.urls import path
from loans import views

app_name = "loans"   
urlpatterns = [
    path("", views.homepage, name="homepage"),

    path("apply", views.create_loan, name="apply"),
    path('user-page', views.userPage, name='user-page'),
    path('loan-types', views.loan_types, name='loan-types'),
    path('applications', views.loans, name='applications'),
    path('all-payments', views.all_payments, name='all-payments'),
    path('loan-payment', views.loanPayment, name='loan-payment'),
    path('amortizations', views.amortizations, name='amortizations'),
]