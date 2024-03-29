# Generated by Django 5.0.2 on 2024-03-05 00:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_hopps'),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='hopps',
            name='description',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='hopps',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='hopps',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='hopps',
            name='equip_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.equipmenttype'),
        ),
    ]
