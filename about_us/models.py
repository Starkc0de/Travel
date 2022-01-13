from django.db import models

# Create your models here.

class About_Us(models.Model):
    about_img = models.ImageField(upload_to='destination_photos', height_field=None,
                                        width_field=None, max_length=None, null=True, blank=True)
    about_title = models.CharField(max_length=50, null=True, blank=True)
    about_disc = models.TextField(null=True, blank=True)
    about_intg = models.IntegerField(null=True, blank=True)
    
class Team_about(models.Model):    
    team_img = models.ImageField(upload_to='destination_photos', height_field=None,
                                        width_field=None, max_length=None, null=True, blank=True)
    team_name = models.CharField(max_length=50, null=True, blank=True)
    team_about = models.CharField(max_length=50, null=True, blank=True)


class about_us_logo(models.Model):
    logo_img = models.ImageField(upload_to='logo_photos', height_field=None,
                                 width_field=None, max_length=None, null=True, blank=True)

    class Meta:
        verbose_name_plural = "About_Logo_img"
        db_table = 'About_Logo_img'
