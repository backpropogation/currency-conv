from django.conf import settings
from django.core.cache import cache
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_429_TOO_MANY_REQUESTS

from apps.currency.models import Rate
from apps.currency.utils import ResponseDetail


@api_view(('POST',))
def update_rate(request):
    """
    Small view to manually refresh Rate. Available only once an hour.
    """
    if not cache.get('updated_hour_ago', False):
        Rate.sync()
        cache.set('updated_hour_ago', True, timeout=settings.UPDATE_TIME_LIMIT)
        return Response(data=ResponseDetail.UPDATE_SUCCESS)
    return Response(
        data=ResponseDetail.UPDATE_FAILED,
        status=HTTP_429_TOO_MANY_REQUESTS
    )
