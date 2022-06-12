# Generated by Django 4.0.1 on 2022-01-11 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_item_options_item_category_alter_item_photo1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_of_item', models.CharField(max_length=11, verbose_name='Id товара')),
                ('name_of_item', models.CharField(max_length=100, verbose_name='Название товара')),
                ('category', models.CharField(max_length=100, verbose_name='Категория')),
                ('price', models.CharField(max_length=20, verbose_name='Цена')),
                ('surname', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('patronymic', models.CharField(max_length=100, verbose_name='Отчество')),
                ('phone', models.CharField(max_length=20, verbose_name='Мобильный телефон')),
                ('city', models.CharField(max_length=100, verbose_name='Город')),
                ('post_office', models.CharField(max_length=100, verbose_name='Отделение')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(max_length=100, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='item',
            name='photo1',
            field=models.ImageField(upload_to='main/img', verbose_name='Фото1'),
        ),
    ]
