# Generated by Django 3.2 on 2022-09-26 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0019_auto_20220915_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.IntegerField(),
        ),
    ]
