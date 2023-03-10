# Generated by Django 4.1.7 on 2023-03-04 22:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contas', '0001_initial'),
        ('condominio', '0002_alter_condominio_fundo_reserva_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leituras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mesano', models.CharField(max_length=6)),
                ('leitura_inical', models.FloatField(default=0)),
                ('leitura_final', models.FloatField(default=0)),
                ('data_leitura', models.DateTimeField(auto_now_add=True)),
                ('conta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contas.contas')),
                ('morador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='condominio.morador')),
            ],
            options={
                'verbose_name': 'Leitura',
                'verbose_name_plural': 'Leituras',
            },
        ),
    ]
