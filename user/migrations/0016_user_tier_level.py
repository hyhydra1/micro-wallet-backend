# Generated by Django 4.2.4 on 2024-02-07 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_alter_userwalletcredential_private_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='tier_level',
            field=models.IntegerField(default=0),
        ),
    ]
