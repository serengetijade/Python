# Generated by Django 2.2.5 on 2022-11-04 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameHoard', '0004_auto_20221104_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='Price',
            field=models.DecimalField(blank=True, decimal_places=2, default='00.00', max_digits=6, null=True),
        ),
    ]