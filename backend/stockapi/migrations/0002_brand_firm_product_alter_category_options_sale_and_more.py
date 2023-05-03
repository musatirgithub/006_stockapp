# Generated by Django 4.1.4 on 2023-05-03 11:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stockapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('image', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Firm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('phone', models.CharField(max_length=25)),
                ('address', models.CharField(max_length=25)),
                ('image', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=25)),
                ('stock', models.PositiveSmallIntegerField(default=0)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_brand', to='stockapi.brand')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stockapi.brand')),
                ('firm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stockapi.firm')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stockapi.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stockapi.brand')),
                ('firm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stockapi.firm')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stockapi.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_category', to='stockapi.category'),
        ),
    ]
