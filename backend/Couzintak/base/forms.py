from django.forms import ModelForm
from .models import Room
from django.contrib.auth.models import User


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
        fields = ['username', 'email']
