# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-07 08:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=200)),
                ('address_line1', models.CharField(max_length=200)),
                ('address_line2', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=2)),
                ('zip_postal', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expense_date', models.DateField()),
                ('description', models.TextField()),
                ('pretax_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tax_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='subsidiary.Category')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='subsidiary.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='expense',
            name='tax',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='subsidiary.Tax'),
        ),
    ]
