from django.db import models
from django.db.models.fields import DateTimeField

class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category',
                                 on_delete=models.CASCADE,
                                 null=True,
                                 default=1,
                                 verbose_name='Наименование категории')

    def __str__(self):
        return f'{self.title}'
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-create_at']

class Category(models.Model):
    title = models.CharField(max_length=200,
                             db_index=True,
                             verbose_name='Наименование категории')
    def __str__(self):
        return  f'{self.title}'


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


