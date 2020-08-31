from django.test import TestCase
from datetime import datetime

from .models import Bill


class BillModelTests(TestCase):

    def test_bill_create_with_supply_is_not(self):
        """
        Объект создается со значением supply (доставлено) == 'Нет' (Ожидаем)
        """
        bill = Bill(product='АКБ', supplier='', clinic='', engineer='')
        self.assertIs(bill.supply == 'Нет', True)

    def test_bill_is_delivered(self):
        """
        Функция delivered переводит объект в состояние supply == Да (Получили)
        """
        bill = Bill(product='АКБ', supplier='', clinic='', engineer='')
        bill.delivered()
        self.assertIs(bill.supply == 'Да', True)

    def test_bill_days_count(self):
        """
        Тестируем функцию расчёта дней прошедших с заказа (order_date) до получения (supply_date)
        Функция days_count отдает количество дней с момента заказа до now().date или до сегодня
        :return:
        """
        order_date_str = '2020-08-20'
        order_date = datetime.strptime(order_date_str, '%Y-%m-%d')
        supply_date_str = '2020-08-29'
        supply_date = datetime.strptime(supply_date_str, '%Y-%m-%d')
        bill = Bill(product='АКБ', supplier='', clinic='', engineer='', supply='Да',
                    supply_date=supply_date,
                    order_date=order_date,)
        self.assertIs(bill.days_count == 9, True)



