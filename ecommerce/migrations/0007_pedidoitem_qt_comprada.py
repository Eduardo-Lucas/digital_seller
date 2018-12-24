# Generated by Django 2.1.3 on 2018-11-28 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0006_auto_20181119_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidoitem',
            name='qt_comprada',
            field=models.DecimalField(decimal_places=4, default=0, help_text='Quantidade comprada (Produto)', max_digits=15),
            preserve_default=False,
        ),
    ]