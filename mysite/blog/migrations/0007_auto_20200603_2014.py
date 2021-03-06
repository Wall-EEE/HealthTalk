# Generated by Django 3.0.6 on 2020-06-03 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200602_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdetailpage',
            name='custom_title',
            field=models.CharField(blank=True, help_text='Overwrites the default title', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='bloglistingpage',
            name='custom_title',
            field=models.CharField(blank=True, help_text='Overwrites the default title', max_length=100, null=True),
        ),
    ]
