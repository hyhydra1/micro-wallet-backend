# Generated by Django 4.2.2 on 2023-07-22 13:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_refer_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='wallet_id',
            new_name='deposit_addr',
        ),
        migrations.CreateModel(
            name='UserWalletCredential',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_address', models.CharField(max_length=50, unique=True)),
                ('private_address', models.CharField(max_length=100, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
