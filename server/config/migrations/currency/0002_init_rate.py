from django.db import migrations

from apps.currency.tasks import get_rate


def init_rate(apps, schema_editor):
    get_rate.delay()


class Migration(migrations.Migration):
    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(init_rate),
    ]
