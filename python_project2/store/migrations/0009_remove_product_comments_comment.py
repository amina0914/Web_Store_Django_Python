# Generated by Django 4.0.4 on 2022-05-04 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_product_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='comments',
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='store.product')),
            ],
        ),
    ]
