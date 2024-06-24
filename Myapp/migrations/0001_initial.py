# Generated by Django 4.2.13 on 2024-06-24 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('tipo_consulta', models.IntegerField(choices=[[0, 'consulta'], [1, 'reclamo'], [2, 'sugerencia'], [3, 'cotizacion']])),
                ('mensaje', models.TextField()),
                ('avisos', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_obra',
            fields=[
                ('medium', models.CharField(max_length=20)),
                ('id_obra', models.AutoField(db_column='idObra', primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Obra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('precio', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('autor', models.CharField(max_length=20)),
                ('imagen', models.ImageField(null=True, upload_to='productos')),
                ('tipo_obra', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Myapp.tipo_obra')),
            ],
        ),
    ]
