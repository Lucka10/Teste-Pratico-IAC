# Generated by Django 4.2.11 on 2024-04-25 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('telefone', models.IntegerField(max_length=18)),
                ('datadenasc', models.DateField(blank=True, null=True, verbose_name='Data de nascimento')),
            ],
        ),
    ]
