from django.db import models


class Item(models.Model):
    name = models.CharField('Название', max_length=100)
    description = models.TextField('Описание')
    category = models.CharField('Категория', max_length=100)
    photo1 = models.ImageField('Фото1', upload_to='main/img')
    photo2 = models.ImageField('Фото2', blank=True, upload_to='main/img')
    photo3 = models.ImageField('Фото3', blank=True, upload_to='main/img')
    photo4 = models.ImageField('Фото4', blank=True, upload_to='main/img')
    photo5 = models.ImageField('Фото5', blank=True, upload_to='main/img')
    price = models.CharField('Цена', max_length=20)

    def __str__(self):
        return self.name

    def name_cut(self):
        return self.name[:25] + '...'

    def get_absolute_url(self):
        return f'{self.id}/buy'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Order(models.Model):
    id_of_item = models.CharField('Id товара', max_length=11)
    name_of_item = models.CharField('Название товара', max_length=100)
    category = models.CharField('Категория', max_length=100)
    price = models.CharField('Цена', max_length=20)
    surname = models.CharField('Фамилия', max_length=100)
    name = models.CharField('Имя', max_length=100)
    patronymic = models.CharField('Отчество', max_length=100)
    phone = models.CharField('Мобильный телефон', max_length=20)
    city = models.CharField('Город', max_length=100)
    post_office = models.CharField('Отделение', max_length=100)

    def __str__(self):
        return self.name_of_item

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
