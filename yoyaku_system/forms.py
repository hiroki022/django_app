from django import forms
from .models import Booking, Camera_manage, Equipment_manage, Booking
from django.utils import timezone
import datetime

class BookingForm(forms.Form):

    camera_name = forms.ModelChoiceField(
        label='camera',
        queryset=Camera_manage.objects.all(),
        required=True,
        widget = forms.RadioSelect()
    )

    equipment_name = forms.ModelChoiceField(
        label='equipment',
        queryset=Equipment_manage.objects.all(),
        required=True,
        widget = forms.RadioSelect()
    )

    rental_start = forms.DateField(
        label='start_day',
        widget=forms.DateTimeInput(attrs={"type": "datetime-local", "value": timezone.datetime.now().strftime('%Y-%m-%dT%H:%M')}),
        input_formats=['%Y-%m-%dT%H:%M']
    )
