# Generated by Django 4.2.4 on 2023-08-10 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_tienda', '0003_rename_prodructo_producto'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria_producto',
            options={'verbose_name': 'categoriaProd', 'verbose_name_plural': 'categoriasProd'},
        ),
    ]