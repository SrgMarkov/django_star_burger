# Generated by Django 3.2.15 on 2023-10-18 06:05

from django.db import migrations
from foodcartapp.models import OrderList


def add_price_to_orders(apps, schema_editor):
    Order = apps.get_model('foodcartapp', 'Order')
    for order in Order.objects.all():
        if not order.price:
            order.price = order.product.price * order.quantity
            order.save()


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0045_alter_order_price'),
    ]

    operations = [
        migrations.RunPython(add_price_to_orders),
    ]