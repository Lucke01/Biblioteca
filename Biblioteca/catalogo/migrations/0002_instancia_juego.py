# Generated by Django 4.2.3 on 2023-12-29 19:30

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='instancia_juego',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='ID unico', primary_key=True, serialize=False)),
                ('finalizacion_beta', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('M', 'Mantenimiento'), ('D', 'Disponible'), ('R', 'Reservado')], default='M', help_text='disponibilidad de la beta del juego', max_length=1)),
                ('juego', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogo.juego')),
            ],
            options={
                'ordering': ['finalizacion_beta'],
            },
        ),
    ]