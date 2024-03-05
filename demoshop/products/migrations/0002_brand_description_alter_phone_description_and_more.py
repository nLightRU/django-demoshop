# Generated by Django 5.0.3 on 2024-03-05 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=2),
        ),
    ]
