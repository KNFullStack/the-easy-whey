# Generated by Django 3.2 on 2022-08-17 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0003_auto_20220817_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='postcode',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
