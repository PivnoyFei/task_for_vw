from datetime import datetime

from django.db import models


class Tag(models.Model):
    name = models.SlugField('Название', max_length=50, unique=True, db_index=True)
    link = models.URLField('Ссылка', max_length=200, unique=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    link = models.URLField('Ссылка', unique=True)
    text = models.TextField('Описание')
    pub_date = models.DateTimeField('Дата публикации', default=datetime.now)
    tags = models.ForeignKey(
        Tag, related_name='news', verbose_name='Тэги', on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('-pub_date', )
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title[:50]
