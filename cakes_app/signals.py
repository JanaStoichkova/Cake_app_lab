import random

from django.db.models.signals import pre_delete
from django.dispatch import receiver

from cakes_app.models import Baker, Cake


@receiver(pre_delete, sender=Baker)
def _on_baker_deleted(sender, instance, **kwargs):
    cakes = Cake.objects.filter(user=instance.user).all()
    for cake in cakes:
        cake.baker = random.choice(Baker.objects.all())
        cake.save()