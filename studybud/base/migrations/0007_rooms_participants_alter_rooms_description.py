# Generated by Django 5.0 on 2023-12-28 09:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0006_alter_messages_options_alter_topic_options"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="rooms",
            name="participants",
            field=models.ManyToManyField(
                related_name="participants", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="rooms",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]