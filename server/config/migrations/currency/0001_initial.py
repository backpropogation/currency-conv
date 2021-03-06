# Generated by Django 2.2.1 on 2019-11-03 12:49

from django.db import migrations, models
import djmoney.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_rate', models.DateTimeField(verbose_name='Rate date')),
                ('base_currency', djmoney.models.fields.CurrencyField(default='EUR', max_length=3, verbose_name='Default currency')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date of request to EU bank')),
                ('EUR', models.DecimalField(decimal_places=4, max_digits=12, verbose_name='EUR')),
                ('USD', models.DecimalField(decimal_places=4, max_digits=12, verbose_name='USD')),
                ('CZK', models.DecimalField(decimal_places=4, max_digits=12, verbose_name='CZK')),
                ('PLN', models.DecimalField(decimal_places=4, max_digits=12, verbose_name='PLN')),
            ],
        ),
    ]
