# Generated by Django 3.2 on 2022-09-15 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('subscription', '0017_rename_subscription_number_subscription_order_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subscriptions', to='profiles.userprofile'),
        ),
    ]
