# Generated by Django 3.1.3 on 2020-12-06 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0002_auto_20201122_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Город'),
        ),
    ]
