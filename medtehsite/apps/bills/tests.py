from django.test import TestCase
from datetime import datetime
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate


from .models import Bill


class BillModelTests(TestCase):

    def setUp(self):

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
        self.assertTrue(bill.days_count == 9)
        self.assertFalse(bill.days_count == 8)


class SigninTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', password='12test12', email='test@example.com')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        user = authenticate(username='test', password='12test12')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='12test12')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_password(self):
        user = authenticate(username='test', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)
