# Generated by Django 2.1.3 on 2018-11-12 17:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0007_auto_20181112_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='dt_alteracao',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produto',
            name='hr_alteracao',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]