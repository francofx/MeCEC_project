# Generated by Django 5.1 on 2024-09-19 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0002_alter_registro_autorizacion_iglesia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
