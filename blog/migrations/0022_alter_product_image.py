# Generated by Django 3.2.7 on 2022-03-03 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_alter_product_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
