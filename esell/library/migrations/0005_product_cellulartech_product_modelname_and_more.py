# Generated by Django 5.0.6 on 2024-05-14 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_product_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cellulartech',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='modelname',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='opertingsys',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
