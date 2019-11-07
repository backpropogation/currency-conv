import requests
from django.conf import settings
from django.db import models
from djmoney.models.fields import CurrencyField


class RateMetaclass(models.base.ModelBase):
    """
    Metaclass for resolving many currencies.
    """
    def __new__(cls, name, bases, attrs):
        for currency in settings.CURRENCIES:
            attrs[f'{currency}'] = models.DecimalField(
                max_digits=settings.MAX_RELATION_TO_CURRENCY_DIGITS,
                decimal_places=settings.DECIMAL_PLACES,
                verbose_name=f"{currency}"
            )
        return super().__new__(cls, name, bases, attrs)


class Rate(models.Model, metaclass=RateMetaclass):
    """
    Main entity for representing rates of currencies.
    """
    date_of_rate = models.DateTimeField(verbose_name='Rate date')
    base_currency = CurrencyField(
        default=settings.DEFAULT_CURRENCY,
        verbose_name='Default currency'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Date of request to EU bank'
    )

    @classmethod
    def sync(cls):
        """
        Method for updating rate from EU CENTRAL BANK information.
        """
        import xml.etree.ElementTree as ET
        response = requests.get(settings.EU_CENTRAL_BANK_URL)
        parsed = ET.fromstring(response.content)
        kwgs = {
            'base_currency': 'EUR',
            'EUR': 1,
            'date_of_rate': parsed[2][0].attrib['time']
        }
        for currency_info in parsed[2][0]:
            code = currency_info.attrib['currency']
            rate = currency_info.attrib['rate']
            if code in settings.CURRENCIES:
                kwgs[code] = rate

        cls.objects.create(
            **kwgs
        )

    def __str__(self):
        return f'Rate {self.date_of_rate.strftime("%d.%m.%Y %H:%M")}'
