# Generated by Django 5.0.1 on 2024-01-17 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='encodings',
            field=models.BinaryField(blank=True, null=True),
        ),
    ]