# Generated by Django 3.0.6 on 2020-07-24 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0004_notification_readed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='readed',
            new_name='readable',
        ),
    ]
