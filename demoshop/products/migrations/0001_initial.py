# Generated by Django 5.0.3 on 2024-03-05 17:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('phone_model', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('brand_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.brand')),
            ],
        ),
    ]
