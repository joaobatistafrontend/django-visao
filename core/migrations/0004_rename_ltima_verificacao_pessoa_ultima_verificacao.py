# Generated by Django 5.0.1 on 2024-01-18 01:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_pessoa_ltima_verificacao_pessoa_total_verificacoes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pessoa',
            old_name='ltima_verificacao',
            new_name='ultima_verificacao',
        ),
    ]