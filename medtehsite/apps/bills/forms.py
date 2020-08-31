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
            'order_author',
            'bill_number',
            'bill_date',
            'bill_sum',
            'comment'
        )
        widgets = {
            'product': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название запчасти'}),
            'supplier': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название поставщика'}),
            'clinic': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название ЛПУ куда пойдёт запчасть'}),
            'device': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Для какого апарата'}),
            'engineer': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Какому технику отдать запчасть'}),
            'supply': forms.Select(attrs={'class': 'form-control'}),
            'order_author': forms.Select(attrs={'class': 'form-control'}),
            'bill_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Номер счёта'}),
            'bill_date': DateInput(attrs={'class': 'form-control'}),
            'bill_sum': forms.NumberInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Комментарий', 'rows': 3}),
        }
