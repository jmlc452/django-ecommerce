# Generated by Django 4.2.4 on 2023-08-25 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_tienda', '0010_rename_imagen_producto_imagen_1_producto_imagen_2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='imagen_2',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='imagen_3',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='imagen_4',
        ),
    ]
