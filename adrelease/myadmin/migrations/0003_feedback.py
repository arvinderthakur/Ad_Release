# Generated by Django 4.1.7 on 2023-03-29 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0002_inquiry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.CharField(max_length=20)),
                ('comment', models.TextField()),
                ('date', models.DateField(auto_now=True)),
                ('customers', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myadmin.customers')),
            ],
            options={
                'db_table': 'feedback',
            },
        ),
    ]
