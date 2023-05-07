# Generated by Django 4.2.1 on 2023-05-06 15:58

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=50)),
                ('waist_min_size', models.PositiveIntegerField()),
                ('waist_max_size', models.PositiveIntegerField(blank=True, null=True)),
                ('hip_min_size', models.PositiveIntegerField()),
                ('hip_max_size', models.PositiveIntegerField(blank=True, null=True)),
                ('height_min_size', models.PositiveIntegerField()),
                ('height_max_size', models.PositiveIntegerField(blank=True, null=True)),
                ('available_count', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique_with=['title'])),
                ('photo_main', models.ImageField(upload_to='product_photos/%Y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, null=True, upload_to='product_photos/%Y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, null=True, upload_to='product_photos/%Y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, null=True, upload_to='product_photos/%Y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, null=True, upload_to='product_photos/%Y/%m/%d/')),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('active', models.BooleanField(default=True)),
                ('sale_count', models.IntegerField(default=0)),
                ('code', models.CharField(editable=False, max_length=40, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('colors', models.ManyToManyField(blank=True, related_name='colors', to='products.product')),
                ('sizes', models.ManyToManyField(to='products.size')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]
