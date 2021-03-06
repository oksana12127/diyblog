# Generated by Django 2.2.12 on 2020-06-06 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200524_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='dislikes',
            field=models.IntegerField(default=0, verbose_name='Не нравится'),
        ),
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.IntegerField(default=0, verbose_name='Нравится'),
        ),
        migrations.AlterField(
            model_name='bloger',
            name='image',
            field=models.ImageField(blank=True, default='no photo', null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='summary',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
