# Generated by Django 3.2.25 on 2024-10-06 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_has_sizes'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]
