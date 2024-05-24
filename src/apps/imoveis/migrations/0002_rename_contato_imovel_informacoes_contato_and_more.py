# Generated by Django 5.0.4 on 2024-05-21 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imovel',
            old_name='contato',
            new_name='informacoes_contato',
        ),
        migrations.RenameField(
            model_name='imovel',
            old_name='quantidade_vagas_carros',
            new_name='quantidade_vagas_garagem',
        ),
        migrations.AlterField(
            model_name='imovel',
            name='resumo',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='imovel',
            name='titulo',
            field=models.CharField(max_length=50),
        ),
    ]