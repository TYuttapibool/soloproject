# Generated by Django 2.2 on 2021-06-21 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JadeHourApp', '0006_auto_20210617_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
