# Generated by Django 4.1.7 on 2023-03-29 08:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0009_add_new_ad_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=100)),
                ('page_no', models.CharField(max_length=100)),
                ('mode', models.CharField(max_length=100)),
                ('order_date', models.DateField()),
                ('date', models.DateField(default=datetime.date.today)),
                ('subject', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('image', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('company', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myadmin.company')),
                ('customers', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myadmin.customers')),
            ],
            options={
                'db_table': 'order',
            },
        ),
    ]
