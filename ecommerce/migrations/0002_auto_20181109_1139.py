# Generated by Django 2.1.3 on 2018-11-09 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marca',
            name='cd_marca',
            field=models.PositiveIntegerField(default=1, unique=True),
        ),
    ]