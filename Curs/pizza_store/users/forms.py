from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import password_validators_help_text_html
from django.contrib.auth.password_validation import validate_password

AuthUser = get_user_model()


class RegisterForm(forms.ModelForm):
    class Meta:
        model = AuthUser
        fields = ['first_name', 'last_name', 'email', 'password']

    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
        required=True,
        help_text=password_validators_help_text_html()
    )

    password_confirmation = forms.CharField(
        label='Password Confirmation',
        widget=forms.PasswordInput,
        required=True,
        help_text='Please confirm your password'
    )

    def save(self, commit=True):
        password = self.cleaned_data['password']
        self.instance.set_password(password)

        return super().save(commit)


class PasswordForm(forms.Form):

    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
        required=True,
        max_length=255,
        help_text='Please confirm your password'
    )

    password_confirmation = forms.CharField(
        label='Password Confirmation',
        widget=forms.PasswordInput,
        required=True,
        max_length=255,
        help_text='Please confirm your password'
    )

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user


    def clean_password(self):
        password = self.cleaned_data.get('password')
        validate_password(password, self.user)

        return password

    def clean_password_confirmation(self):
        password = self.cleaned_data['password']
        password_confirmation = self.cleaned_data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Password not confirmed!')

        return password_confirmation

    def save(self):
        password = self.cleaned_data['password']
        self.user.set_password(password)
        self.user.save()