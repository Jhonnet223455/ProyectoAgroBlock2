# Generated by Django 4.2.6 on 2023-10-17 17:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Agro_app', '0005_agricultural_product_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agricultural_product',
            name='image',
            field=models.FileField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='harvester',
            name='image',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
