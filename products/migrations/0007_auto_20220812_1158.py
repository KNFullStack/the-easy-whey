# Generated by Django 3.2 on 2022-08-12 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20220802_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nutrition',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nutrition', to='products.product'),
        ),
        migrations.DeleteModel(
            name='Ingredient',
        ),
    ]
