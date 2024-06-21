# Generated by Django 5.0.6 on 2024-06-21 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_presentation_alter_documents_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documents',
            name='link',
        ),
        migrations.AddField(
            model_name='documents',
            name='document',
            field=models.FileField(null=True, upload_to='documents', verbose_name='Материал'),
        ),
    ]
