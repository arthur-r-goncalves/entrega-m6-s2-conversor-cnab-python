# Generated by Django 4.1.2 on 2022-10-06 17:16

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="File",
            fields=[
                ("id", models.BigIntegerField(primary_key=True, serialize=False)),
                ("file", models.FileField(upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "type",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(9),
                            django.core.validators.MinLengthValidator(1),
                        ]
                    ),
                ),
                (
                    "date",
                    models.CharField(
                        max_length=8,
                        validators=[django.core.validators.MinLengthValidator(8)],
                    ),
                ),
                (
                    "hour",
                    models.CharField(
                        max_length=6,
                        validators=[django.core.validators.MinLengthValidator(6)],
                    ),
                ),
                (
                    "value",
                    models.CharField(
                        max_length=10,
                        validators=[django.core.validators.MinLengthValidator(10)],
                    ),
                ),
                (
                    "cpf",
                    models.CharField(
                        max_length=11,
                        validators=[django.core.validators.MinLengthValidator(11)],
                    ),
                ),
                (
                    "card",
                    models.CharField(
                        max_length=12,
                        validators=[django.core.validators.MinLengthValidator(12)],
                    ),
                ),
                (
                    "store_owner",
                    models.CharField(
                        max_length=14,
                        validators=[django.core.validators.MinLengthValidator(14)],
                    ),
                ),
                (
                    "store_name",
                    models.CharField(
                        max_length=19,
                        validators=[django.core.validators.MinLengthValidator(19)],
                    ),
                ),
            ],
        ),
    ]