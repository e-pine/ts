# Generated by Django 5.0.2 on 2024-03-05 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_equipmenttype_hopps_description_hopps_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hopps',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
