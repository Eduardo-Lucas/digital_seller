# Generated by Django 2.1.3 on 2018-11-08 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cd_marca', models.PositiveIntegerField(default=1, max_length=11, unique=True)),
                ('nm_marca', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
                'ordering': ['nm_marca'],
            },
        ),
        migrations.CreateModel(
            name='Versao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
