# Generated by Django 4.2.11 on 2024-04-25 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='telefone',
            field=models.IntegerField(),
        ),
    ]
