# Generated by Django 4.0.2 on 2022-02-25 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_gestao', '0005_rename_data_gastos_data_referente'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorias',
            name='cor',
            field=models.CharField(default='#fff', max_length=16),
            preserve_default=False,
        ),
    ]
