# Generated by Django 5.0.3 on 2024-03-05 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_rename_phone_model_phone_model_phone_color_phone_ram_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smartwatch',
            name='series',
        ),
        migrations.AddField(
            model_name='smartwatch',
            name='strap_color',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
