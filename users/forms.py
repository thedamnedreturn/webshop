from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=False,  # Делаем email необязательным
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email (необязательно)'})
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']  # Убрали 'phone'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Добавляем классы Bootstrap ко всем полям
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label