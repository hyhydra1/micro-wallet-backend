# Generated by Django 4.2.2 on 2023-07-23 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transfer',
            old_name='value',
            new_name='amount',
        ),
        migrations.AlterField(
            model_name='depositwithdraw',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='swap',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
