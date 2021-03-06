# Generated by Django 2.2 on 2020-09-12 13:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_dogs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dogs',
            name='age',
        ),
        migrations.AddField(
            model_name='dogs',
            name='birthday',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='дата рождения'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dogs',
            name='arrived_at',
            field=models.DateField(verbose_name='дата прибытия'),
        ),
    ]
