# Generated by Django 5.0.2 on 2024-03-05 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_hopps_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hopps',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
