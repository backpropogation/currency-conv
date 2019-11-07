from django.conf import settings


def extract_exchange_rates(obj):
    """
    Helper method of getting all currencies from Rate obj.
    :param obj: Rate object
    :return: Dictionary
    """

    return {currency: getattr(obj, currency) for currency in settings.CURRENCIES}
