# Generated by Django 4.0.2 on 2022-02-25 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_gestao', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gastos',
            name='data',
            field=models.DateField(auto_now=True),
        ),
    ]
