# Generated by Django 4.2 on 2023-04-14 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vemsapp', '0005_rename_eventdetails_addevents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addevents',
            name='latest_event',
            field=models.BooleanField(default=False, help_text='o-default,1-latest'),
        ),
    ]