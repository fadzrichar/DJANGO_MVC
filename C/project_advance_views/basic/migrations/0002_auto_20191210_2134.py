# Generated by Django 3.0 on 2019-12-10 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='pub_date',
            field=models.DateField(blank=True, default=None, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_content',
            field=models.TextField(blank=True, default=None, max_length=2000),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_title',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image_path',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
    ]
