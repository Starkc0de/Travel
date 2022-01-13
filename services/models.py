from django.db import models

# Create your models here.

class ServiceModel(models.Model):

    img = models.ImageField(upload_to='destination_photos', height_field=None,
                                        width_field=None, max_length=None, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    title = models.CharField(max_length=50, null=True, blank=True )


class Service_logo(models.Model):
    logo_img = models.ImageField(upload_to='logo_photos', height_field=None,
                                 width_field=None, max_length=None, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Service_logo_img"
        db_table = 'Service_logo_img'
