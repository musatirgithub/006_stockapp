from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Purchase, Sale


@receiver(pre_save, sender=Purchase)
def calculate_total_price(sender, instance, **kwargs):
    instance.total_price = instance.quantity * instance.price


@receiver(pre_save, sender=Sale)
def calculate_total_price(sender, instance, **kwargs):
    instance.total_price = instance.quantity * instance.price
