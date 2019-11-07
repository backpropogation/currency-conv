import random

from django.test import TestCase

from apps.currency.models import Rate


class RateTestCase(TestCase):
    def test_rate_sync(self):
        self.assertEqual(Rate.objects.count(), 0)
        rate_obj_count = random.randint(1, 50)
        for _ in range(rate_obj_count):
            Rate.sync()
        self.assertEqual(Rate.objects.count(), rate_obj_count)
