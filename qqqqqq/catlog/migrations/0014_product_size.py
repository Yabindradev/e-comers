# Generated by Django 3.2.16 on 2022-11-09 11:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('catlog', '0013_auto_20221107_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL')], default=1, max_length=4),
            preserve_default=False,
        ),
    ]
