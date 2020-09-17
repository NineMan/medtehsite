from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from .models import Bill
from .forms import BillForm
import logging


logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'bills/index.html')


def bill_list(request):

    display = request.GET.get('display')
    if display == 'all':
        bills = Bill.objects.all()
    elif display == 'supply':
        bills = get_list_or_404(Bill, supply='Да')
    else:
        bills = get_list_or_404(Bill, supply='Нет')
    logger.debug(bills)

    return render(request, 'bills/bill_list.html', {'bills': bills})


def bill_detail(request, pk):

    pk_first = Bill.objects.all().first().pk
    pk_last = Bill.objects.all().last().pk

    try:
        bill = Bill.objects.get(pk=pk)
    except Bill.DoesNotExist:
        return render(request, 'bills/bill_not_found.html', {'pk': pk, 'pk_first': pk_first, 'pk_last': pk_last})
    logger.debug('user read bill')
    logger.debug(bill)

    return render(request, 'bills/bill_detail.html', {'bill': bill, 'pk': pk, 'pk_first': pk_first, 'pk_last': pk_last})


@login_required
def bill_new(request):

    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            print('form is valid')
            bill = form.save()
            bill.order_author = request.user
            bill.save()
            return redirect('bills:bill_detail', pk=bill.pk)
        else:
            print('form not valid')
    else:
        form = BillForm()

    return render(request, 'bills/bill_new.html', {'form': form})


@login_required
def bill_edit(request, pk):

    bill = get_object_or_404(Bill, pk=pk)
    if request.method == 'POST':
        form = BillForm(request.POST, instance=bill)
        # Проверка формы
        if form.is_valid():
            bill = form.save()
            return redirect('bills:bill_detail', pk=bill.pk)
    else:
        form = BillForm(instance=bill)

    return render(request, 'bills/bill_edit.html', {'form': form, 'bill': bill})


@login_required
def bill_delivered(request, pk):

    bill = get_object_or_404(Bill, pk=pk)
    bill.delivered()

    return redirect('bills:bill_detail', pk=pk)


def bill_detail_prev(request, pk):

    if pk > 1:
        pk -= 1
    return redirect('bills:bill_detail', pk=pk)


def bill_detail_next(request, pk):

    pk += 1
    return redirect('bills:bill_detail', pk=pk)


def test(request):
    """ Для тестовых разработок """
    bill = Bill.objects.get(pk=3)
    form = BillForm(instance=bill)
    return render(request, 'test/test.html', {'form': form, 'bill': bill})
