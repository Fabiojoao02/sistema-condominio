# Generated by Django 4.1.7 on 2023-03-07 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('condominio', '0003_morador_apto_sala'),
    ]

    operations = [
        migrations.AddField(
            model_name='condominio',
            name='mostrar',
            field=models.BooleanField(default=True),
        ),
    ]
