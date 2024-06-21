# Generated by Django 5.0.6 on 2024-06-21 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_metodics'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Дата')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('order', models.FileField(upload_to='documents', verbose_name='Приказ')),
                ('members', models.FileField(upload_to='documents', verbose_name='Участники')),
                ('results', models.FileField(blank=True, null=True, upload_to='documents', verbose_name='Итоги')),
            ],
            options={
                'verbose_name': 'Конкурс',
                'verbose_name_plural': 'Конкурсы',
            },
        ),
    ]
