from django import forms
from .models import Person, Phone


class PersonForm(forms.ModelForm):
    birth_date = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y',
                               attrs={'class': 'form-control datepicker'}),
        input_formats=('%d/%m/%Y',)
    )

    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'birth_date', 'email', 'address', 'complement',
                  'district', 'city', 'pase', 'consulta', 'aporte', 'blocked']


class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = ['phone', 'phone_type']
