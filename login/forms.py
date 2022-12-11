from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm 
from django.contrib.auth.models import User

class CustomerSignupForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ('first_name', 'last_name','username', 'email','password1', 'password2')


class CustomerLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')



class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("username", "email")

