from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Модель пользователя.
    """

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.username}'


class Presentation(models.Model):
    """
    Модель презентаций.
    """
    title = models.CharField('Название', max_length=155)
    link = models.URLField('url')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Презентация'
        verbose_name_plural = 'Презентации'

    def __str__(self):
        return f'{self.title}'


class Materials(models.Model):
    """
    Модель видеомамтериалов.
    """
    title = models.CharField('Название', max_length=155)
    link = models.URLField('url')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Видеоматериал'
        verbose_name_plural = 'Видеоматериалы'

    def __str__(self):
        return f'{self.title}'


class Documents(models.Model):
    """
    Модель нормативных документов.
    """
    title = models.CharField('Название', max_length=155)
    link = models.URLField('url')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

    def __str__(self):
        return f'{self.title}'
