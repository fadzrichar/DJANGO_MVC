# Generated by Django 3.0 on 2019-12-09 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hewan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('species', models.CharField(max_length=12)),
                ('berat', models.IntegerField(default=0)),
                ('umur', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Kandang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('isi_kandang', models.CharField(max_length=255)),
                ('luas_kandang', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Pengunjung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('nomor_telepon', models.CharField(max_length=255)),
                ('hari_berkunjung', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Penjaga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('nomor_telepon', models.IntegerField(default=0)),
                ('jadwal_jaga', models.CharField(max_length=255)),
            ],
        ),
    ]
