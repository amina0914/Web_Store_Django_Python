# Generated by Django 4.0.4 on 2022-05-01 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_product_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='owner',
            field=models.CharField(default='no owner', max_length=100),
        ),
    ]
