# Generated by Django 3.2.7 on 2022-02-17 10:01

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0013_auto_20220215_2102'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cartitem',
            new_name='Cart',
        ),
    ]