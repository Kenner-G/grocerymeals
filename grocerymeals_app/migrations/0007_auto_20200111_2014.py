# Generated by Django 2.2.3 on 2020-01-11 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocerymeals_app', '0006_auto_20200111_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='formatted_title',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='product',
            name='provider',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]
