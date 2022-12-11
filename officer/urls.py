from django.urls import path
from officer import views


app_name = 'officer'
urlpatterns = [
    path('admin-login', views.superuser_login_view, name='admin-login'),
    path('admin-logout', views.superuser_logout_view, name='logout'),
    path('admin-page', views.adminPage, name='admin-page'),

    path('create-customer', views.create_customer, name='create-customer'),
    path('edit-customer/<str:pk>/', views.edit_customer, name='edit-customer'),
    path('delete-customer/<str:pk>/', views.delete_customer, name='delete-customer'),
    path('all-customers', views.customers, name='all-customers'),

    path('user-group', views.user_group, name='user-group'),
    path('add-user', views.add_user, name='add-user'),
    path('all-users', views.users, name='all-users'),
    path('edit-user/<str:pk>/', views.edit_user, name='edit-user'),
    path('delete-user/<str:pk>/', views.delete_user, name='delete-user'),

    path('payments', views.all_payments, name='payments'),
    path('create-payment', views.create_payment, name='create-payment'),
    path('edit-payment/<str:pk>/', views.edit_payment, name='edit-payment'),
    path('delete-payment/<str:pk>/', views.delete_payment, name='delete-payment'),
    
    path('loan-types', views.loan_types, name='loan-types'),
    path('create-type', views.add_loan_type, name='create-type'),
    path('edit-type/<str:pk>/', views.edit_loan_type, name='edit-type'),
    path('delete-type/<str:pk>/', views.delete_loan_type, name='delete-type'),
    
    path('all-loans', views.loans, name='all-loans'),
    path('edit-loan/<str:pk>/', views.edit_loan, name='edit-loan'),
    path('delete-loan/<str:pk>/', views.delete_loan, name='delete-loan'),

    path('all-amortizations', views.all_amortizations, name='all-amortizations'),
    path('create-amortization', views.create_amortization, name='create-amortization'),
    path('edit-amortization/<str:pk>/', views.edit_amortization, name='edit-amortization'),
    path('delete-amortization/<str:pk>/', views.delete_amortization, name='delete-amortization'),
]