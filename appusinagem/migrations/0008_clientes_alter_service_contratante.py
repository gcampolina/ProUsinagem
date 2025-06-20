# Generated by Django 5.1.4 on 2025-06-16 15:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appusinagem', '0007_alter_service_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('telefone', models.CharField(max_length=15)),
                ('endereco', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='service',
            name='contratante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appusinagem.clientes'),
        ),
    ]
