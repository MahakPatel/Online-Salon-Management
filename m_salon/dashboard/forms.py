from django.forms import ModelForm

from appoinment.models import Booking
from home.models import register


class OrderForm(ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'


class CustomerForm(ModelForm):
    class Meta:
        model = register
        fields = '__all__'
        exclude = ['user','password','confirm']
