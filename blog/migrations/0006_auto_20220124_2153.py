# Generated by Django 3.2.7 on 2022-01-24 16:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_auto_20220107_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Изображение'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст комментария')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор коментария')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.product', verbose_name='Пост')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
