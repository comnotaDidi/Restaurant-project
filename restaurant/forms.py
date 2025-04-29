from django import forms
from .models import Reservation
from .models import Review 
from .models import User
from django.contrib.auth.forms import UserCreationForm

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'email', 'date', 'time', 'guests', 'comment']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'email', 'message', 'rating']
        widgets = {
            'rating': forms.RadioSelect
        }


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label="Логин")
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, label='Имя')
    last_name = forms.CharField(max_length=100, label='Фамилия')
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2025)), label='Дата рождения')
    email = forms.EmailField(max_length=100, label='Электронная почта')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'birth_date', 'email', 'username', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password1")
        confirm_password = cleaned_data.get("password2")

        if password != confirm_password:
            raise forms.ValidationError("Пароли не совпадают")

        return cleaned_data