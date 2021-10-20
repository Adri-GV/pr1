# Generated by Django 3.2.8 on 2021-10-18 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0003_alter_pedido_customer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pedido',
            options={'verbose_name': 'Pedido', 'verbose_name_plural': 'Pedidos'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
        migrations.AlterField(
            model_name='pedido',
            name='customer',
            field=models.IntegerField(verbose_name='Cliente'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='products',
            field=models.CharField(max_length=1000, verbose_name='Productos'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='total',
            field=models.FloatField(verbose_name='Total'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='null', upload_to='products', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(verbose_name='Precio'),
        ),
    ]
