# Generated by Django 4.2 on 2023-04-15 02:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vemsapp', '0009_alter_eventdetails_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventregisteration',
            name='eventreg',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vemsapp.eventdetails'),
        ),
    ]