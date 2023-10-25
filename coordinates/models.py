import datetime

from django.db import models


class AddressCoordinates(models.Model):
    address = models.CharField(
        verbose_name='Адрес',
        max_length=100,
    )
    lon = models.FloatField(
        verbose_name='Долгота',
        null=True
    )
    lat = models.FloatField(
        verbose_name='Широта',
        null=True
    )
    coordinates_date = models.DateField(
        verbose_name='Дата запроса координат',
        default=datetime.date.today()
    )

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'