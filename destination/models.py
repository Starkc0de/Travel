from django.db import models
from autoslug import AutoSlugField

# Create your models here.


class DestinationModel(models.Model):

    place_img = models.ImageField(upload_to='destination_photos', height_field=None,
                                  width_field=None, max_length=None, null=True, blank=True)
    place_name = models.CharField(max_length=50)

    about_place = models.CharField(max_length=200)
    place_rate = models.CharField(max_length=50)
    Testimonials = models.TextField(null=True, blank=True)
    client_name = models.CharField(max_length=50, null=True, blank=True)
    latest_news_photo = models.ImageField(upload_to='latest_news_photos', height_field=None,
                                          width_field=None, max_length=None, null=True, blank=True)
    latest_travelling_date = models.DateField(null=True, blank=True)
    news_post_text = models.TextField(null=True, blank=True)
    slug = AutoSlugField(populate_from='destination_name',
                         null=True, blank=True)

    def __str__(self):
        return str(self.destination_name)
