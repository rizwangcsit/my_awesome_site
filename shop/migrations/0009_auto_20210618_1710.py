# Generated by Django 3.1.6 on 2021-06-18 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_orderupdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discription',
            field=models.CharField(max_length=500),
        ),
    ]
