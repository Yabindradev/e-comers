# Generated by Django 3.2.16 on 2022-11-04 09:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('catlog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
    ]