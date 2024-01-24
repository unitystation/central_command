# Generated by Django 3.2.23 on 2024-01-24 16:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_passwordresetrequestmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_confirmed',
            field=models.BooleanField(default=False, help_text='Has this account been confirmed via email?', verbose_name='Confirmed'),
        ),
        migrations.CreateModel(
            name='AccountConfirmation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]