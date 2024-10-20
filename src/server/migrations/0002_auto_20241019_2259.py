# Generated by Django 3.2.25 on 2024-10-20 01:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serverinformation',
            name='description',
            field=models.CharField(help_text='A brief description of what this server is about', max_length=200, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='serverinformation',
            name='listing_key',
            field=models.CharField(blank=True, help_text='A unique key used for listing this server. Do not lose this key!', max_length=30, null=True, unique=True, verbose_name='Listing Key'),
        ),
        migrations.AlterField(
            model_name='serverinformation',
            name='motd',
            field=models.CharField(help_text='Message displayed to players when they join the server', max_length=255, verbose_name='Message of the Day (MOTD)'),
        ),
        migrations.AlterField(
            model_name='serverinformation',
            name='name',
            field=models.CharField(help_text='Name this server uses to present itself in the servers list', max_length=50, verbose_name='Name'),
        ),
        migrations.CreateModel(
            name='ServerTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50, verbose_name='Name')),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='server.serverinformation')),
            ],
        ),
    ]
