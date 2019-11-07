from rest_framework import routers
from apps.currency.viewsets import CurrencyConverter

router = routers.DefaultRouter()

router.register('currency', CurrencyConverter, base_name='conventer')
