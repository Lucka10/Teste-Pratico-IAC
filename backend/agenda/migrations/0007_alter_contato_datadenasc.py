# Generated by Django 4.2.11 on 2024-04-28 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0006_alter_contato_datadenasc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='datadenasc',
            field=models.DateField(default='2000-01-01', verbose_name='Data de nascimento'),
        ),
    ]
