# Generated by Django 3.2 on 2022-08-30 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('subscription', '0011_subscription_is_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='profiles.userprofile'),
        ),
    ]
