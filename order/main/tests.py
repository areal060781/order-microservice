from dateutil.relativedelta import relativedelta

from django.test import TestCase
from django.utils import timezone

from .models import OrderCustomer, Order
from .status import Status

from .exceptions import OrderAlreadyCompletedError
from .exceptions import OrderCancellationError
from .exceptions import InvalidArgumentError


class OrderModelTestCase(TestCase):

    @classmethod
    def setUPTestData(cls):
        cls.customer_001 = OrderCustomer.objects.create(
            customer_id=1,
            email='customer_001@test.co,'
        )

        Order.objects.create(order_customer=cls.customer_001)
        Order.objects.create(order_customer=cls.customer_001, status=Status.Completed.value)

        cls.customer_002 = OrderCustomer.objects.create(
            customer_id=2,
            email='customer_002@test.com'
        )

        Order.objects.create(order_customer=cls.customer_002)

    def test_cancel_order(self):
        order = Order.objects.get(pk=1)

        self.assertIsNotNone(order)
        self.assertEqual(Status.Received.value, order.status)

        Order.objects.cancel_order(order)
        self.assertEqual(Status.Cancelled.value, order.status)

    def test_cancel_completed_order(self):
        order = Order.objects.get(pk=2)

        self.assertIsNotNone(order)
        self.assertEqual(Status.Completed.value, order.status)

        with self.assertRaises(OrderCancellationError):
            Order.objects.cancel_order(order)

    def test_cancel_order_sith_invalid_argument(self):
        with self.assertRaises(InvalidArgumentError):
            Order.objects.cancel_order({'id': 1})

    def test_get_all_orders_by_customer(self):
        orders = Order.objects.get_all_orders_by_customer(customer_id=1)

        self.assertEqual(2, len(orders), msg='It should have returned 2 orders.')

    def test_get_all_orders_by_customer_with_invalid_id(self):
        with self.assertRaises(InvalidArgumentError):
            Order.objects.get_all_orders_by_customer('o')

    def test_get_customer_incomplete_orders(self):
        orders = Order.objects.get_customer_incomplete_orders(customer_id=1)

        self.assertEqual(1, len(orders))
        self.assertEqual(Status.Received.value, orders[0].status)

    def test_get_customer_incomplete_orders_with_invalid_id(self):
        with self.assertRaises(InvalidArgumentError):
            Order.objects.get_customer_incomplete_orders('o')