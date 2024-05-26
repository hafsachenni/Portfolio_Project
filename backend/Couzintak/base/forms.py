from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Room, User, Contact
from django import forms


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']

class RoomForm(ModelForm):
    """we creating a form that will allow us to create a room
    based on some values/fields in our table"""
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']


class UserForm(ModelForm):
    """this is a form that enables loged in users to edit their accs"""
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email', 'bio']


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Full Name', 'required': True}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Address', 'required': True}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject', 'required': True}),
            'message': forms.Textarea(attrs={'placeholder': 'Message', 'cols': 30, 'rows': 5, 'required': True}),
        }