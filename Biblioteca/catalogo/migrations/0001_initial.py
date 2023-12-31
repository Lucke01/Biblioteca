# Generated by Django 4.2.3 on 2023-12-29 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Ingrese el nombre del genero (p.ej: Accion, Supervivencia,etc)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_empresa', models.CharField(max_length=200)),
                ('desarrolladores', models.CharField(max_length=200)),
                ('año_de_salida', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Juego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('sumario', models.TextField(help_text='Ingrese una descripcion del juego', max_length=1000)),
                ('genero', models.ManyToManyField(help_text='Seleccione un genero para este juego', to='catalogo.genero')),
                ('marca', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogo.marca')),
            ],
        ),
    ]
