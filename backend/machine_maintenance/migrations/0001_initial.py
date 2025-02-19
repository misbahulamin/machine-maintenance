# Generated by Django 5.1.2 on 2024-11-17 09:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('model_number', models.CharField(max_length=255, unique=True)),
                ('purchase_date', models.DateTimeField()),
                ('block_no', models.IntegerField()),
                ('line_no', models.IntegerField()),
                ('location', models.CharField(max_length=255)),
                ('last_breakdown_start', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Running', 'Running'), ('Under Maintenance', 'Under Maintenance'), ('Broken', 'Broken')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mechanic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
                ('assigned_line', models.IntegerField()),
                ('assigned_block', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BreakdownLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_category', models.CharField(max_length=255)),
                ('breakdown_start', models.DateTimeField()),
                ('lost_time', models.DurationField()),
                ('comments', models.TextField()),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='machine_maintenance.machine')),
                ('mechanic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='machine_maintenance.mechanic')),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='machine_maintenance.operator')),
            ],
        ),
    ]
