# Generated by Django 5.0.3 on 2024-03-10 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_remove_phone_series'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='cpu',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='display_size',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='ram',
            field=models.IntegerField(default=4),
        ),
    ]