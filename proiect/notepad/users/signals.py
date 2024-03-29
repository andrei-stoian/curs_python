from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.db import transaction
from django.contrib.auth import get_user_model
from .models import Activation
from .views import send_activation_email

AuthUserModel = get_user_model()


@receiver(pre_save, sender=AuthUserModel)
def inactivate_user(sender, instance, **kwargs):
    if not instance.pk:
        instance.is_active = False
        instance.password = "123444112"


@receiver(post_save, sender=AuthUserModel)
def create_activation(sender, instance, created, **kwargs):
 
    try:
        with transaction.atomic():
            if created:
                Activation(user=instance).save()
                print(instance.email)
                send_activation_email(instance)
    except ValueError:
        AuthUserModel.objects.get(pk=instance.id).delete()