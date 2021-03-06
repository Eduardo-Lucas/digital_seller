# Generated by Django 2.1.3 on 2018-11-15 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='nm_razao_social',
            field=models.CharField(blank=True, help_text='Razão social para pessoa jurídica', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nr_cnpj',
            field=models.CharField(blank=True, help_text='CNPJ', max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nr_cpf',
            field=models.CharField(blank=True, help_text='CPF', max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nr_inscricao_estadual',
            field=models.CharField(blank=True, help_text='Inscrição estadual para pessoa jurídica', max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nr_rg',
            field=models.CharField(blank=True, help_text='Registro geral', max_length=15, null=True),
        ),
    ]
