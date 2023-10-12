# Generated by Django 4.2.4 on 2023-10-12 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_product_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(default=' ', max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='amount',
            field=models.IntegerField(default=1),
        ),
    ]