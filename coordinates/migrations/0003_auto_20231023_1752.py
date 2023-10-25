# Generated by Django 3.2.15 on 2023-10-23 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coordinates', '0002_auto_20231023_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addresscoordinates',
            name='address',
            field=models.CharField(default='', max_length=100, verbose_name='Адрес'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='addresscoordinates',
            name='lat',
            field=models.FloatField(null=True, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='addresscoordinates',
            name='lon',
            field=models.FloatField(null=True, verbose_name='Долгота'),
        ),
    ]