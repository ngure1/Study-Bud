# Generated by Django 4.2.8 on 2023-12-24 10:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0003_messages_user_rooms_host"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="rooms",
            options={"ordering": ["-updated", "-created"]},
        ),
    ]
