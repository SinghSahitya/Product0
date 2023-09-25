from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Seller, Customer, Order, Item, User

class SellerSignUpForm(UserCreationForm):
    username = forms.CharField(max_length=150, help_text='Required. Enter a username', widget=forms.TextInput(attrs={'placeholder': 'Your Username'}))
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.',  widget=forms.EmailInput(attrs={'placeholder': 'Your Email'}))
    first_name = forms.CharField(max_length=30, help_text='Required. Enter your first name.', widget=forms.TextInput(attrs={'placeholder': 'Your First Name'}) )
    last_name = forms.CharField(max_length=30, help_text='Required. Enter your last name.', widget=forms.TextInput(attrs={'placeholder': 'Your Last Name'}) )
    phone = forms.CharField(max_length=20, help_text='Required. Enter your phone number.', widget=forms.TextInput(attrs={'placeholder': 'Your Phone Number'}) )
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Your Address'}), help_text='Required. Enter your address.')

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password1', 'password2')



class ItemForm(forms.ModelForm):
    title = forms.CharField(max_length=150)
    available_units = forms.IntegerField()
    class Meta:
        model = Item
        fields = {'title', 'available_units' }