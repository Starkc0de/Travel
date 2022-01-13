from django.db import models
from autoslug import AutoSlugField

# Create your models here.


class HomePageModel(models.Model):

    destination_img = models.ImageField(upload_to='destination_photos', height_field=None,
                                        width_field=None, max_length=None, null=True, blank=True)
    destination_name = models.CharField(max_length=50)
    special_offer = models.BooleanField()
    about_destination = models.CharField(max_length=200)
    destination_rate = models.CharField(max_length=50)
    Testimonials = models.TextField(null=True, blank=True)
    client_name = models.CharField(max_length=50, null=True, blank=True)
    latest_news_photo = models.ImageField(upload_to='latest_news_photos', height_field=None,
                                          width_field=None, max_length=None, null=True, blank=True)
    latest_travelling_date = models.DateField(null=True, blank=True)
    news_post_text = models.TextField(null=True, blank=True)
    slug = AutoSlugField(populate_from='destination_name',
                         always_update=True,  db_column="slug", null=True, blank=True)

    def __str__(self):
        return str(self.destination_name)

    class Meta:
        verbose_name_plural = "Destination_Data"
        db_table = 'Destination_Data'


class home_logo(models.Model):
    logo_img = models.ImageField(upload_to='logo_photos', height_field=None,
                                 width_field=None, max_length=None, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Home_Logo"
        db_table = 'Home_Logo'


class home_des(models.Model):
    page_des = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Home_Des"
        db_table = 'Home_Des'
