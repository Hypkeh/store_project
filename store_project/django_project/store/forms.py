from django import forms
from django.forms import ModelForm
from .models import Product, Order
from django.contrib.auth.models import User


class SearchForm(forms.Form):
    q = forms.CharField(max_length=20, label='Поиск по словам')


class ProductForm(ModelForm):

    class Meta:
        model = Product
        fields = '__all__'


class OrderForm(ModelForm):

    class Meta:
        model = Order
        fields = '__all__'


class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label='Пароль', required=False, widget=forms.widgets.PasswordInput())
    password2 = forms.CharField(label='Пароль (повторно)', required=False)
    is_client = forms.NullBooleanSelect()
 #   rate = forms.FloatField()
 #   number_of_goods = forms.IntegerField(widget=forms.widgets.NumberInput())
    desired_date = forms.DateField(widget=forms.widgets.DateInput())
 #   choice = forms.ChoiceField(choices=(('f', 'first'), ('s', 'second')))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', )

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = '__all__'


class ImageForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('image',)