from django.db import models
import secrets
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from .utils.constants import ACTIVATION_AVAILABILITY
from django.contrib.auth.models import AbstractUser


AuthUserModel = get_user_model()



AVAILABILITY = {
    ACTIVATION_AVAILABILITY['unit']: ACTIVATION_AVAILABILITY['value']
}


def generate_token():
    return secrets.token_urlsafe(32)[:32]


class Activation(models.Model):
    user = models.OneToOneField(AuthUserModel, related_name="activation", on_delete=models.CASCADE)
    token = models.CharField(
        max_length=64,
        null=True,
        unique=True,
        default=None,
    )
    expires_at = models.DateTimeField(
        default=None
    )
    activated_at = models.DateTimeField(default=None, null=True)

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = secrets.token_urlsafe(32)
            self.expires_at = timezone.now() + timezone.timedelta(**AVAILABILITY)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.user)

    def __repr__(self):
        return f"{self.user} - {self.token}"