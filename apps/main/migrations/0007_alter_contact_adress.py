# Generated by Django 5.1.4 on 2025-01-06 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='adress',
            field=models.CharField(max_length=255, verbose_name='Адресс'),
        ),
    ]
