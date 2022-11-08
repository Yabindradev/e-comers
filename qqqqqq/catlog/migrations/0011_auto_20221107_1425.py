# Generated by Django 3.2.16 on 2022-11-07 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catlog', '0010_auto_20221107_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='instructions',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Post_Zip_code',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='second_line_of_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='third_line_of_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]