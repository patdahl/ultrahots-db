# Generated by Django 5.1.3 on 2024-11-30 17:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarMake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Casting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('make', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ultrahots.carmake')),
            ],
        ),
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('collector_number', models.CharField(blank=True, default='', max_length=255)),
                ('toy_number', models.CharField(blank=True, default='', max_length=255)),
                ('color', models.CharField(max_length=255)),
                ('casting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ultrahots.casting')),
            ],
        ),
    ]
