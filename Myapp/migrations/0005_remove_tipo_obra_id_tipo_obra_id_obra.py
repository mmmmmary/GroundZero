# Generated by Django 4.2.13 on 2024-06-24 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0004_obra_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipo_obra',
            name='id',
        ),
        migrations.AddField(
            model_name='tipo_obra',
            name='id_obra',
            field=models.AutoField(db_column='idGenero', default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
