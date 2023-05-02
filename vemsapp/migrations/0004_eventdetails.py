# Generated by Django 4.2 on 2023-04-14 17:57

from django.db import migrations, models
import vemsapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('vemsapp', '0003_alter_events_year_table_alter_upload_event_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='eventdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=50)),
                ('event_date', models.DateField()),
                ('small_desc', models.CharField(max_length=250)),
                ('event_type', models.CharField(max_length=50)),
                ('event_image', models.ImageField(blank=True, null=True, upload_to=vemsapp.models.getfilename)),
                ('latest_event', models.BooleanField(default=False, help_text='o-show,1-hidden')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'event',
            },
        ),
    ]