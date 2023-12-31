# Generated by Django 4.2.2 on 2023-06-20 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(db_index=True, max_length=100, unique=True, verbose_name='Product Name')),
                ('description', models.CharField(max_length=300, verbose_name='Product Description')),
                ('price', models.DecimalField(decimal_places=4, max_digits=10, verbose_name='Product Price')),
                ('quantity', models.IntegerField(verbose_name='Product Quantity')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]
