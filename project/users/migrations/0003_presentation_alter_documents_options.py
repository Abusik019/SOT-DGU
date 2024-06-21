# Generated by Django 5.0.6 on 2024-06-21 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_documents'),
    ]

    operations = [
        migrations.CreateModel(
            name='Presentation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('material', models.FileField(upload_to='presentations', verbose_name='Материал')),
            ],
            options={
                'verbose_name': 'Презентация',
                'verbose_name_plural': 'Презентации',
            },
        ),
        migrations.AlterModelOptions(
            name='documents',
            options={'verbose_name': 'Документ', 'verbose_name_plural': 'Документы'},
        ),
    ]
