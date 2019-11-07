from django.conf import settings
from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.currency.models import Rate


@receiver(post_save, sender=Rate)
def update_cache(instance, **kwargs):
    """
    Caching every rate after save for faster access.
    """

    cache.set('latest_rate', instance, timeout=settings.RATE_TIMELIFE)
