# Generated by Django 3.2.22 on 2024-01-18 20:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_passwordresetrequestmodel_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='passwordresetrequestmodel',
            name='expiry_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
