# Generated by Django 4.2 on 2023-04-14 19:37

from django.db import migrations, models
import django.db.models.deletion
import vemsapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('vemsapp', '0006_alter_addevents_latest_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='eventdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('last_date', models.DateField()),
                ('auditorium', models.CharField(max_length=50)),
                ('img', models.ImageField(blank=True, null=True, upload_to=vemsapp.models.getfilename)),
                ('clg_name', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=550)),
                ('invitation', models.FileField(blank=True, null=True, upload_to=vemsapp.models.getfilename)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('addevent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vemsapp.addevents')),
            ],
            options={
                'db_table': 'eventdetails',
            },
        ),
    ]
