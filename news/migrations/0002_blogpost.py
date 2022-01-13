# Generated by Django 3.2.9 on 2022-01-02 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postimg', models.ImageField(blank=True, null=True, upload_to='destination_photos')),
                ('auther', models.CharField(blank=True, max_length=50, null=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('blog', models.TextField(blank=True, null=True)),
                ('postdatetime', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
