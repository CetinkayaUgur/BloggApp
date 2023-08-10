from django.contrib.auth.forms import UserCreationForm
from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=70)
    password = forms.CharField(max_length=50)


class RegisterForm(forms.Form):
    user_name = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=70)
    password = forms.CharField(max_length=50)
    confirm_password = forms.CharField(max_length=50)

    def clean(self):
        user_name = self.cleaned_data.get("user_name")
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Aynı parolayı gir lütfen")

        values = {"user_name":user_name, "password":password, "first_name":first_name, "last_name":last_name, "email":email}

        return values

    # if password and confirm_password or password != confirm_password:
    #     raise forms.ValidationError("Passwords don't match  ୧༼ ಠ益ಠ ༽୨")
