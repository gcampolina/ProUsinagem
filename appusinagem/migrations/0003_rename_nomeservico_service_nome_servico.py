# Generated by Django 5.1.4 on 2024-12-14 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appusinagem', '0002_rename_servico_service_nomeservico'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='nomeservico',
            new_name='nome_servico',
        ),
    ]
