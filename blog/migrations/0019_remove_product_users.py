# Generated by Django 3.2.7 on 2022-02-17 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_rename_user_product_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='users',
        ),
    ]
