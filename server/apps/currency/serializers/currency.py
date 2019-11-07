from django.conf import settings
from rest_framework import serializers

from apps.currency.models import Rate
from apps.currency.utils import convert_currencies, extract_exchange_rates


class CurrencyReadSerializer(serializers.Serializer):
    """
    Read serializer for detecting bad requests.
    """
    from_currency = serializers.ChoiceField(settings.CURRENCIES)
    amount = serializers.DecimalField(
        max_digits=11,
        decimal_places=2
    )

    def validate_amount(self, amount):
        """
        Validating amount of money.
        """
        if amount > settings.MAX_CONVERT_AMOUNT:
            raise serializers.ValidationError("Too big number. Try again.")
        elif amount <= 0:
            raise serializers.ValidationError("Make number positive.")
        return amount


class CurrencyExchangeSerializer(serializers.ModelSerializer):
    """
    Exchange serializer, values passed to this class are already correct.
    """
    exchange_rates = serializers.SerializerMethodField()
    converted_currencies = serializers.SerializerMethodField()

    class Meta:
        model = Rate
        fields = ('exchange_rates', 'converted_currencies')

    def get_exchange_rates(self, obj):
        return extract_exchange_rates(obj)

    def get_converted_currencies(self, obj):
        return convert_currencies(obj, self.context['from_currency'], self.context['amount'])
