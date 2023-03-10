# Generated by Django 4.1.7 on 2023-02-15 15:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(unique=True, verbose_name='Название')),
                ('link', models.URLField(unique=True, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Тэг',
                'verbose_name_plural': 'Тэги',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('link', models.URLField(unique=True, verbose_name='Ссылка')),
                ('text', models.TextField(verbose_name='Описание')),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата публикации')),
                ('tags', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news', to='parser.tag', verbose_name='Тэги')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ('-pub_date',),
            },
        ),
    ]
