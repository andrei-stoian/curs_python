from django.db import transaction
from django.contrib.auth.signals import user_logged_in
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from users.models import Activation
from users.views.activation import send_activation_email
from utils.cart import Cart



AuthUserModel = get_user_model()


@receiver(pre_save, sender=AuthUserModel)
def inactivate_user(instance, **kwargs):
    is_social_user = hasattr(instance, 'is_social_auth') and instance.is_social_auth is True
    if not instance.pk and not is_social_user:
        instance.is_active = False
        instance.password = None


@receiver(post_save, sender=AuthUserModel)
def create_activation(sender, instance, created, **kwargs):
    print('!!! Signal post_save was triggered!')
    try:
        with transaction.atomic():
            if created:
                Activation(user=instance).save()
                send_activation_email(instance)
    except ValueError:
        AuthUserModel.objects.get(pk=instance.id).delete()


@receiver(user_logged_in)
def get_cart_data(request, user, **kwargs):
    Cart.load(user, request.session)
