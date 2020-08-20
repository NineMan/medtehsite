from django import forms
from .models import Bill


class DateInput(forms.DateInput):
    input_type = 'date'


class BillForm(forms.ModelForm):

    # product1 =

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
            'product': forms.TextInput(attrs={'size': '38px'}),
            'supplier': forms.TextInput(attrs={'size': '38px'}),
            'clinic': forms.TextInput(attrs={'size': '38px'}),
            'device': forms.TextInput(attrs={'size': '38px'}),
            'engineer': forms.TextInput(attrs={'size': '38px'}),
            # 'supply',
            # 'bill_number',
            'bill_date': DateInput(),
            'comment': forms.Textarea(attrs={'rows': 3, 'cols': 50, 'margin': '-50px'}),
        }
