# Generated by Django 3.2.16 on 2022-11-07 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catlog', '0006_auto_20221107_0725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.CharField(choices=[('KHOTANG', 'khotang')], max_length=30),
        ),
    ]
