from django import forms
from django.contrib.auth.password_validation import password_validators_help_text_html
from django.contrib.auth import get_user_model
from .models import Notes
from django import forms


AuthUser = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control'}))



class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title','text']

class NoteEditForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title','text']