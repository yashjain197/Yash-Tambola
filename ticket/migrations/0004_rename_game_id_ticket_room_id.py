# Generated by Django 5.0.1 on 2024-01-18 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0003_ticket_set_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='game_id',
            new_name='room_id',
        ),
    ]
