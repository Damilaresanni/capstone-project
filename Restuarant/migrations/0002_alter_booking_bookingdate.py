# Generated by Django 4.2.1 on 2023-06-13 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restuarant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='bookingDate',
            field=models.DateTimeField(),
        ),
    ]
