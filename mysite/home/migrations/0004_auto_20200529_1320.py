# Generated by Django 3.0.6 on 2020-05-29 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_body'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homepage',
            options={'verbose_name': 'Home Page', 'verbose_name_plural': 'Home Pages'},
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='body',
        ),
        migrations.AddField(
            model_name='homepage',
            name='banner_title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
