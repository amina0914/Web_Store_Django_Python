# Generated by Django 4.0.4 on 2022-05-09 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_product_flags'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='rating',
            field=models.PositiveSmallIntegerField(choices=[(1, '1 - VERY BAD'), (2, '2 - BAD'), (3, '3 - AVERAGE'), (4, '4 - GOOD'), (5, '5 - VERY GOOD')], default=1),
            preserve_default=False,
        ),
    ]
