# Generated by Django 3.2.7 on 2022-02-11 14:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0009_cartitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='city',
            field=models.CharField(default=django.utils.timezone.now, max_length=255, verbose_name='Город'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='country',
            field=models.CharField(default=2, max_length=255, verbose_name='Страна'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Profie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=255, verbose_name='Имя профиля')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Номер')),
                ('country', models.CharField(max_length=255, verbose_name='Страна')),
                ('city', models.CharField(max_length=255, verbose_name='Город')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Ник профиля')),
            ],
        ),
    ]