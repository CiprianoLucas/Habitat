# Generated by Django 5.1 on 2024-09-19 23:39

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=3000)),
                ('type', models.CharField(choices=[('R', 'RECLAMAÇÃO'), ('M', 'MANUTENÇÃO'), ('O', 'OUTROS')], default='O', max_length=1)),
                ('status', models.CharField(choices=[('A', 'ANDAMENTO'), ('C', 'CONCLUIDO'), ('P', 'PENDENTE')], default='P', max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Requisição',
                'verbose_name_plural': 'Requisições',
            },
        ),
    ]
