# Generated by Django 3.0.6 on 2020-06-01 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmediasettings',
            name='twitter',
            field=models.URLField(blank=True, help_text='Instagram URL', null=True),
        ),
    ]
