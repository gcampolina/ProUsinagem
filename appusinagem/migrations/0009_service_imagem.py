# Generated by Django 5.1.4 on 2025-06-16 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appusinagem', '0008_clientes_alter_service_contratante'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='servicos/'),
        ),
    ]
