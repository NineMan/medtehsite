from django.db import models
from django.contrib.auth.models import User

from datetime import date


class Person(User):
    class Meta:
        proxy = True

    def __str__(self):
        return self.last_name


class Bill(models.Model):

    BOOL = {
        ('Да', 'Получили'),
        ('Нет', 'Ожидаем'),
    }

    product = models.CharField(max_length=200,          # Запчасть. Краткое название запчасти (товара, услуги и т.д.)
                               verbose_name='Название запчасти')
    supplier = models.CharField(max_length=50,          # Поставщик. Краткое название организации у которой заказали
                                verbose_name='Поставщик')
    clinic = models.CharField(max_length=50,            # Больница. Для ремонта в которой нужна з/часть
                              verbose_name='ЛПУ')
    device = models.CharField(max_length=100,           # Аппарат на который пойдут запчасти
                              blank=True,
                              verbose_name='Аппарат')
    engineer = models.CharField(max_length=50,          # Техник (инженер), которому нужно отдать запчасть.
                                verbose_name='Техник')
    # -------------------------
    supply = models.CharField(max_length=5,             # Состояние поставки. "Да" если заказ доставлен
                              choices=BOOL,
                              default='Нет',
                              verbose_name='Состояние поставки заказа')
    supply_date = models.DateField(blank=True,          # Дата доставки. Появляется если есть поставка.
                                   auto_now=True,
                                   editable=False,
                                   null=True,
                                   verbose_name='Дата прихода заказа')
    order_date = models.DateField(auto_now_add=True,    # Дата создания заказа (передачи в оплату)
                                  verbose_name='Дата создания заказа')
    bill_number = models.CharField(max_length=50,       # Номер счёта. Не обязательное
                                   blank=True,
                                   verbose_name='Номер счёта')
    bill_date = models.DateField(blank=True,            # Дата указанная в счете. Не обязательное
                                 null=True,
                                 verbose_name='Дата счёта')
    bill_sum = models.DecimalField(max_digits=9,        # Сумма в счёте. Не обязательная
                                   decimal_places=2,
                                   blank=True,
                                   null=True,
                                   verbose_name='Сумма в счёте')
    comment = models.TextField(blank=True,              # Комментарий к заказу
                               verbose_name='Комментарий')

    def __str__(self):
        return str(self.pk) + ' ' + str(self.product) + ' для ' + str(self.clinic)

    class Meta:

        ordering = ['pk']

        verbose_name = 'Заказ по счёту'
        verbose_name_plural = 'Заказы по счёту'

