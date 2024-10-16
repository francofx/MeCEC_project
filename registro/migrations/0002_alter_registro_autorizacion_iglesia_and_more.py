# Generated by Django 5.1 on 2024-08-08 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='autorizacion_iglesia',
            field=models.FileField(upload_to='static/autorizaciones/'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='foto',
            field=models.ImageField(upload_to='static/fotos/'),
        ),
    ]