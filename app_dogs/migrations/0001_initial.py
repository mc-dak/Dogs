# Generated by Django 2.2 on 2020-09-10 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150, verbose_name='кличка')),
                ('age', models.CharField(max_length=20, verbose_name='возраст')),
                ('arrived_at', models.DateTimeField(auto_now_add=True, verbose_name='дата прибытия')),
                ('weight', models.CharField(max_length=20, verbose_name='вес')),
                ('height', models.CharField(max_length=20, verbose_name='рост')),
                ('special', models.TextField(max_length=1000, verbose_name='особые приметы')),
            ],
        ),
    ]
