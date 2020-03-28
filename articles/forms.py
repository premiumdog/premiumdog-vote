from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Article
from django.utils.translation import ugettext_lazy as _
import random
class UserRegisterForm(UserCreationForm):
     
   
    username = forms.CharField(label="Felhasználónév", help_text='Példa: nagysandor vagy nagysandor1 vagy nagy.sandor vagy nagy.sandor1')
    email = forms.EmailField(label="Email cím", help_text='Példa: nagysandor@gmail.com')
    password1 = forms.CharField(widget=forms.PasswordInput(), label="Jelszó", help_text='Példa: Nagysandor1 vagy Nagy.sandor12')
    password2 = forms.CharField(widget=forms.PasswordInput(), label="Jelszó újra",help_text='Írja be újra a jelszót.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        