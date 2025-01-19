from django import forms
from .models import User

class UserRegister(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, min_length=8, label="Введите пароль")
    repeat_password = forms.CharField(widget=forms.PasswordInput, min_length=8, label="Повторите пароль")

    class Meta:
        model = User
        fields = ['username', 'password', 'repeat_password', 'age', 'email']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        repeat_password = cleaned_data.get("repeat_password")

        if password and repeat_password and password != repeat_password:
            raise forms.ValidationError("Пароли не совпадают")

        return cleaned_data