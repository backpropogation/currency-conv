from decimal import Decimal, ROUND_UP
from django.conf import settings


def convert_currencies(obj, from_currency, amount):
    """
    Helper function for converting currencies from base currency.
    :param obj: Rate object
    :param from_currency: Currency needed to be converted
    :param amount: Amount of money
    :return: Dictionary of converted currencies
    """

    return {
        currency: Decimal((
                getattr(obj, currency)
                * amount
                / getattr(obj, from_currency)).quantize(Decimal('.0001'), rounding=ROUND_UP))
        for currency in settings.CURRENCIES
    }
