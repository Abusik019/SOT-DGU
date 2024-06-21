from django.db import models
from django.contrib.auth.models import AbstractUser
from django.templatetags.static import static


class User(AbstractUser):
    pass


class Documents(models.Model):
    title = models.CharField('Название', max_length=255)
    document = models.FileField('Материал', upload_to='documents', null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'


class Presentation(models.Model):
    title = models.CharField('Название', max_length=255)
    material = models.FileField('Материал', upload_to='presentations')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Презентация'
        verbose_name_plural = 'Презентации'


class Video(models.Model):
    title = models.CharField('Название', max_length=255)
    link = models.URLField('link')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Видеоматериал'
        verbose_name_plural = 'Видеоматериалы'


class Metodics(models.Model):
    title = models.CharField('Название', max_length=255)
    material = models.FileField('Материал', upload_to='metodics')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Методичка'
        verbose_name_plural = 'Методички'


class Contest(models.Model):
    date = models.DateField('Дата')
    title = models.CharField('Название', max_length=255)
    order = models.FileField('Приказ', upload_to='documents')
    members = models.FileField('Участники', upload_to='documents')
    results = models.FileField('Итоги', upload_to='documents', null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Конкурс'
        verbose_name_plural = 'Конкурсы'
