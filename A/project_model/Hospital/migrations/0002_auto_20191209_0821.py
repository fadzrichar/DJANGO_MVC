# Generated by Django 3.0 on 2019-12-09 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pasien',
            name='nomor_telepon',
            field=models.CharField(max_length=12),
        ),
    ]
