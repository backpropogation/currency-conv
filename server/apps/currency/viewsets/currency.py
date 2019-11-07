from django.core.cache import cache
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from apps.currency.models import Rate
from apps.currency.serializers import CurrencyReadSerializer, CurrencyExchangeSerializer


class CurrencyConverter(viewsets.ModelViewSet):
    """
    General endpoint for converting values.
    """

    queryset = Rate.objects.all()
    serializer_class = CurrencyReadSerializer

    def create(self, request, *args, **kwargs):
        if not self.queryset.exists():
            return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        latest_rate = self.queryset.last() if cache.get('latest_rate', False) else cache.get('latest_rate')
        exchange_rates = CurrencyExchangeSerializer(
            latest_rate,
            context={
                'amount': serializer.validated_data['amount'],
                'from_currency': serializer.validated_data['from_currency']
            }
        ).data

        return Response(exchange_rates)