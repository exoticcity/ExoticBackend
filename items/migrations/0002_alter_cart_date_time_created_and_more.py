# Generated by Django 5.0.2 on 2024-07-24 11:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='date_time_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 7, 24, 16, 42, 25, 135094), null=True),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='date_time_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 7, 24, 16, 42, 25, 136092), null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='BarCode',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='BaseUnitOfMeasure',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='Brand',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='GTIN',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='ItemCategoryCode',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='ItemSubCategoryCode',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='LastDateTimeModified',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 24, 16, 42, 25, 134090)),
        ),
        migrations.AlterField(
            model_name='product',
            name='Packaging',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='ParentCategory',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='PurchasingCode',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='SalesUnitOfMeasure',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='Type',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='WeightDescription',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
