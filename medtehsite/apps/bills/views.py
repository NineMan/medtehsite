from django.http import Http404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Bill
from .forms import BillForm


def bill_list(request):

    display = request.GET.get('display')
    if display == 'all':
        bills = Bill.objects.all()
    elif display == 'supply':
        bills = Bill.objects.filter(supply='Да')
    else:
        bills = Bill.objects.filter(supply='Нет')

    return render(request, 'bills/bill_list.html', {'bills': bills})


def bill_detail(request, pk):

    if request.method == 'POST':
        bill = Bill.objects.get(pk=pk)
        bill.supply = 'Да'
        bill.supply_date = timezone.now()
        bill.save()
    else:
        """
        Обрабатываю "пустую" страницу
        """
        pk_last = request.META.get('HTTP_REFERER', '')
        if pk_last:
            pk_last = pk_last.split('/')[-1]
        else:
            pk_last = Bill.objects.all().last().pk

        try:
            bill = Bill.objects.get(pk=pk)
        except Bill.DoesNotExist:
            return render(request, 'bills/bill_not_found.html', {'pk': pk_last})

    return render(request, 'bills/bill_detail.html', {'bill': bill})


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

    bill = Bill.objects.get(pk=pk)
    if request.method == 'POST':
        form = BillForm(request.POST, instance=bill)

        # Проверка заказа: "Заказ доставлен?"   (лучше перенести в бизнес-логику)
        if form.instance.supply == "Да":
            bill.supply_date = timezone.now()
        elif form.instance.supply == "Нет":
            bill.supply_date = None

        # Проверка формы
        if form.is_valid():
            bill = form.save()
            bill.save()
            return redirect('bills:bill_detail', pk=bill.pk)
        else:
            pass                                                        # Прописать на случай невалидности формы.

    else:
        form = BillForm(instance=bill)
    print('In bill edit')

    return render(request, 'bills/bill_edit.html', {'form': form, 'bill': bill})


def test(request):
    bill = Bill.objects.get(pk=3)
    form = BillForm(instance=bill)
    return render(request, 'test/test.html', {'form': form, 'bill': bill})


def test2(request):
    bill = Bill.objects.get(pk=2)
    form = BillForm(instance=bill)
    # if request.method == 'POST':
    #     form = BillForm(request.POST, instance=bill)
    #     if form.instance.supply == "Да":
    #         bill.supply_date = timezone.now()
    #     elif form.instance.supply == "Нет":
    #         bill.supply_date = None
    #
    #     if form.is_valid():
    #         bill = form.save()
    #         bill.save()
    #         return redirect('bills:bill_detail', pk=bill.pk)
    # else:
    #     form = BillForm(instance=bill)

    return render(request, 'test/test2.html', {'form': form, 'bill': bill})


def test3(request):
    return render(request, 'test/test3.html')
