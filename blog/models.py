from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
from django.contrib.auth.models import User



#Категория
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

#Продукт
class Product(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name='Пользователь')
    category = models.ManyToManyField(Category,verbose_name='Категория')
    name = models.CharField(max_length=200, db_index=True,verbose_name="Название")
    slug = models.SlugField(max_length=200, db_index=True,verbose_name="Ссылка")
    image = models.ImageField("Изображение")
    description = models.TextField("Описание")
    price = models.DecimalField("Цена" ,max_digits=10, decimal_places=2)
    moderate = models.BooleanField(default=False,verbose_name="Модерация")
    created = models.DateTimeField(default = timezone.now,verbose_name="Опубликовано")
    country=models.CharField(max_length=255,verbose_name='Страна')
    city=models.CharField(max_length=255,verbose_name='Город')
    phone=models.CharField(max_length=15, blank=True, null=True, verbose_name='Номер')

    #Вывод по id и ссылки
    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug':self.slug})
    
    class Meta:
        ordering = ('name',)
        index_together = (('slug'),)

    def __str__(self):
        return self.name

class Comment(models.Model):
    text = models.TextField('Текст комментария')
    date = models.DateTimeField('Дата', default=timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = 'Автор коментария')
    post = models.ForeignKey(Product, on_delete = models.CASCADE, verbose_name = 'Пост')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
    

class Cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    date=models.DateTimeField(default=timezone.now)


class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,verbose_name='Ник профиля')
    surname=models.CharField(max_length=255, verbose_name='Фамилия')
    name=models.CharField(max_length=255, verbose_name='Имя профиля')
    phone=models.CharField(max_length=15, blank=True, null=True, verbose_name='Номер')
    avatar = models.ImageField('Аватар', blank=True, null=True)
    country=models.CharField(max_length=255,verbose_name='Страна')
    city=models.CharField(max_length=255,verbose_name='Город')

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name + ' | ' + self.user.username

class Application(models.Model):
    something=models.CharField('Что-то',max_length=225)

