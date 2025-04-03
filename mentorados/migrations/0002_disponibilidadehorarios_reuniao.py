# Generated by Django 5.1.7 on 2025-04-02 12:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentorados', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DisponibilidadeHorarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicial', models.DateTimeField(blank=True, null=True)),
                ('agendado', models.BooleanField(default=False)),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reuniao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(choices=[('G', 'Gestão'), ('M', 'Marketing'), ('RH', 'Gestão de pessoas'), ('I', 'Impostos')], max_length=2)),
                ('descricao', models.TextField()),
                ('data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mentorados.disponibilidadehorarios')),
                ('mentorado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mentorados.mentorados')),
            ],
        ),
    ]
