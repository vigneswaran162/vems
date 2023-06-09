# Generated by Django 4.2 on 2023-04-18 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vemsapp', '0013_registerevent'),
    ]

    operations = [
        migrations.CreateModel(
            name='event_announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=150)),
                ('issuses', models.CharField(max_length=150)),
                ('desc', models.CharField(max_length=1000)),
                ('event', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
