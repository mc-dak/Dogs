import datetime

from django import forms
from app_dogs.models import Dogs

from dogs import settings


def present_or_future_date(value):
    if value < datetime.date.today():
        raise forms.ValidationError("Дата не может быть в прошлом!")
    return value


class DogsForm(forms.ModelForm):

    birthday = forms.DateField(label="Дата рождения", input_formats=settings.DATE_INPUT_FORMATS, initial="YYYY-MM-DD")
    arrived_at = forms.DateField(label="Дата прибытия в приют", input_formats=settings.DATE_INPUT_FORMATS,
                                 initial="YYYY-MM-DD", validators=[present_or_future_date])

    class Meta:
        model = Dogs
        fields = ['name', 'birthday', 'arrived_at', 'weight', 'height', 'special']


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
