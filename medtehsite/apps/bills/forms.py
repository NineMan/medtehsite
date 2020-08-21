from django import forms
from .models import Bill


class DateInput(forms.DateInput):
    input_type = 'date'


class BillForm(forms.ModelForm):

    class Meta:
        model = Bill
        fields = (
            'product',
            'supplier',
            'clinic',
            'device',
            'engineer',
            'supply',
            'bill_number',
            'bill_date',
            'bill_sum',
            'comment'
        )
        widgets = {
            'product': forms.TextInput(attrs={'size': '36px'}),
            'supplier': forms.TextInput(attrs={'size': '36px'}),
            'clinic': forms.TextInput(attrs={'size': '36px'}),
            'device': forms.TextInput(attrs={'size': '36px'}),
            'engineer': forms.TextInput(attrs={'size': '36px'}),
            'bill_date': DateInput(),
            'comment': forms.Textarea(attrs={'rows': 3, 'cols': 40, 'margin': '-50px'}),
        }
