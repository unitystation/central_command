# Generated by Django 3.2.9 on 2021-11-19 05:18

import accounts.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_identifier',
            field=models.CharField(help_text="Account identifier is used to identify your account. This will be used for bans, job bans, etc and can't ever be changed", max_length=28, primary_key=True, serialize=False, validators=[accounts.validators.AccountNameValidator()], verbose_name='Account identifier'),
        ),
        migrations.AlterField(
            model_name='account',
            name='characters_data',
            field=models.JSONField(default=dict, help_text='Characters data is used to store all the characters associated with this account.', verbose_name='Characters data'),
        ),
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(help_text='Email address must be unique. It is used to login and confirm the account.', max_length=254, unique=True, verbose_name='Email address'),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_authorized_server',
            field=models.BooleanField(default=False, help_text='Can this account broadcast the server state to the server list api? Can this account write to persistence layer?', verbose_name='Authorized server'),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_verified',
            field=models.BooleanField(default=False, help_text='Is this account verified to be who they claim to be? Are they famous?!', verbose_name='Verified'),
        ),
        migrations.AlterField(
            model_name='account',
            name='legacy_id',
            field=models.CharField(blank=True, default='null', help_text="Legacy ID is used to identify your account in the old database. This is used for bans, job bans, etc and can't ever be changed", max_length=28, verbose_name='Legacy ID'),
        ),
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(help_text='Public username is used to identify your account publicly and shows in OOC. This can be changed at any time', max_length=28, validators=[accounts.validators.UsernameValidator()], verbose_name='Public username'),
        ),
    ]
