# Generated by Django 5.0.6 on 2024-05-15 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_remove_product_categories'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]
