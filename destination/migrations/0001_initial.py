# Generated by Django 3.2.9 on 2022-01-01 06:03

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DestinationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_img', models.ImageField(blank=True, null=True, upload_to='destination_photos')),
                ('place_name', models.CharField(max_length=50)),
                ('about_place', models.CharField(max_length=200)),
                ('place_rate', models.CharField(max_length=50)),
                ('Testimonials', models.TextField(blank=True, null=True)),
                ('client_name', models.CharField(blank=True, max_length=50, null=True)),
                ('latest_news_photo', models.ImageField(blank=True, null=True, upload_to='latest_news_photos')),
                ('latest_travelling_date', models.DateField(blank=True, null=True)),
                ('news_post_text', models.TextField(blank=True, null=True)),
                ('slug', autoslug.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from='destination_name')),
            ],
        ),
    ]
