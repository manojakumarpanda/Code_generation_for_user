from django import forms
from django.core.validators import ValidationError
from .models import profile,User_codes,User


class admininput(forms.Form):
    code_num=forms.IntegerField()

    def clean(self):
        code=super().clean()
        if code.get('code_num') == 0:
            raise ValidationError('This cannot be 0 give some other number')
        return code.get('code_num')

class User_form(forms.Form):

    def clean(self):
        cleaned_data = super().clean()
        passw = cleaned_data.get("password")
        passw2 = cleaned_data.get("repassword")
        if passw != passw2:
            raise forms.ValidationError('password is mismatched::')

        return passw
    def clean_email(self):

        email=self.cleaned_data.get('email')
        val_email = email.split('@')
        qs=User.objects.filter(email=email)
        if qs:
            raise forms.ValidationError('This email has registered already::')

        elif val_email[0] in ['gmail.com','email.com']:
            raise forms.ValidationError('This is invalid type of the gmail')
        else:
            return email


    mobile_num =forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'+91-7292929289'}),label='Enter mobile number')
    repassword = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'********'}), label='Re-enter password')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'********'}), label='Enter password')
    username=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder':'Username'}),label='Enter Username')
    first_name=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder':'First Name'}),label='Enter First name')
    last_name=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder':'Last Name'}),label='Enter Lastname')
    email =forms.CharField(max_length=50,widget=forms.EmailInput(attrs={'placeholder':'email@email.com'}),label='Enter email')


class Login_form(forms.Form):
    username = forms.CharField(max_length=50, label='username', widget=forms.TextInput(
        attrs={
            'placeholder': ' Username/email '
        }
    ))
    password = forms.CharField(max_length=50,
                               label='password',
                               widget=forms.PasswordInput(
                                   attrs={'placeholder': ' Enter password Here'}
                               )

                               )