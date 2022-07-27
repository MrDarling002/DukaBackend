# Generated by Django 3.2.7 on 2022-02-17 13:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0016_remove_product_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='user',
            field=models.ForeignKey(default=11, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
