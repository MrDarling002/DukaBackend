# Generated by Django 3.2.7 on 2022-03-03 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_remove_product_moderate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Изображение'),
        ),
    ]
