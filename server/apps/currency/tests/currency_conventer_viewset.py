import random

from django.conf import settings
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.currency.models import Rate
from apps.currency.utils import rand_string


class CurrencyConventerTests(APITestCase):
    def setUp(self):
        self.url = reverse('conventer-list')

    def test_statuses(self):
        """
        Test statuses for different data.
        """

        data = {'from_currency': 'EUR', 'amount': random.randint(1, 1000000)}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
        data = {'from_currency': rand_string(random.randint(0, 100)), 'amount': random.randint(1, 1000000)}
        Rate.sync()
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        data = {'from_currency': random.choice(settings.CURRENCIES), 'amount': random.randint(1, 1000000)}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_response_content(self):
        """
        Ensure that viewset returns ALL supported currencies.
        """

        Rate.sync()
        data = {'from_currency': 'EUR', 'amount': random.randint(1, 1000000)}
        response = self.client.post(self.url, data, format='json')
        currencies_from_exchange_rates = tuple(currency for currency in response.data['exchange_rates'].keys())
        currencies_from_converted_currencies = tuple(currency for currency in response.data['converted_currencies'].keys())
        self.assertEqual(currencies_from_converted_currencies, settings.CURRENCIES)
        self.assertEqual(currencies_from_exchange_rates, settings.CURRENCIES)
