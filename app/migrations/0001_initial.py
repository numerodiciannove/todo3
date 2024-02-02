# Generated by Django 4.2.9 on 2024-02-02 16:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tag",
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
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Task",
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
                ("content", models.CharField(max_length=255)),
                ("datetime", models.DateTimeField(auto_now_add=True)),
                (
                    "deadline",
                    models.DateTimeField(
                        blank=True,
                        default=datetime.datetime(
                            2024, 2, 9, 16, 15, 41, 864223, tzinfo=datetime.timezone.utc
                        ),
                        null=True,
                    ),
                ),
                ("is_complete", models.BooleanField(default=False)),
                (
                    "tags",
                    models.ManyToManyField(
                        blank=True, related_name="tasks", to="app.tag"
                    ),
                ),
            ],
            options={
                "ordering": ["is_complete", "-datetime"],
            },
        ),
    ]
