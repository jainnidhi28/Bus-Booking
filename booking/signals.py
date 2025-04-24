from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Booking

@receiver(post_save, sender=Booking)
def notify_new_booking(sender, instance, created, **kwargs):
    if created:
        print(f"New Booking Created by {instance.user.first_name} {instance.user.last_name} for Bus {instance.bus.bus_number}")