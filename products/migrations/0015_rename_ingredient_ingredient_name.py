# Generated by Django 3.2 on 2022-08-25 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20220825_1146'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredient',
            old_name='ingredient',
            new_name='name',
        ),
    ]
