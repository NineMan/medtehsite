from django import forms
from .models import Bill


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
            'comment'
        )
        widgets = {
            'device': forms.TextInput(attrs={'margin-down': '0px', 'value': ''}),
            'comment': forms.Textarea(attrs={'rows': 3, 'cols': 50, 'margin': '-50px'}),
        }
