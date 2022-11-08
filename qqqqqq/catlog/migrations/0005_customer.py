# Generated by Django 3.2.16 on 2022-11-07 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catlog', '0004_product_is_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_stock', models.BooleanField(default=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('first_line_of_address', models.CharField(max_length=255)),
                ('second_line_of_address', models.CharField(max_length=255)),
                ('third_line_of_address', models.CharField(max_length=255)),
                ('title', models.CharField(choices=[], max_length=30)),
            ],
        ),
    ]