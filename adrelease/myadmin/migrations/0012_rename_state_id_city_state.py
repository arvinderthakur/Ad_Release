# Generated by Django 4.1.7 on 2023-03-29 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0011_alter_company_city_alter_company_state'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='state_id',
            new_name='state',
        ),
    ]
