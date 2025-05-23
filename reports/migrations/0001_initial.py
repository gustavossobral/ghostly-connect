# Generated by Django 5.2.1 on 2025-05-20 21:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('postagens', '0002_comentarios'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.CharField(max_length=1000)),
                ('data', models.DateField(auto_now_add=True)),
                ('postagem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postagens.postagens')),
            ],
        ),
    ]
