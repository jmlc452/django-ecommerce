# Generated by Django 4.2.4 on 2023-08-15 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tienda', '0005_color_producto_talla_producto_producto_color_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='descripcin',
            field=models.TextField(null=True),
        ),
    ]
