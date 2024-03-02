# Generated by Django 5.0.1 on 2024-02-26 18:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Activation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "token",
                    models.CharField(
                        default=None, max_length=64, null=True, unique=True
                    ),
                ),
                ("expires_at", models.DateTimeField(default=None)),
                ("activated_at", models.DateTimeField(default=None, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="activation",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]