from django.urls import path
from login import views


app_name = 'login'
urlpatterns = [
    path('customer-login', views.login_view, name='customer-login'),
    path('customer-signup', views.sign_up_view, name='customer-signup'),
    path('customer-logout', views.logout_view, name='logout'),
    path('customer-details', views.customer_details, name='customer-details'),
    path('edit-details/<str:pk>/', views.edit_details, name='edit-details'),
]