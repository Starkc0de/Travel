from django.db import models
from autoslug import AutoSlugField


# Create your models here.
class Blogpost(models.Model):
    postimg = models.ImageField(upload_to='destination_photos', height_field=None,
                                        width_field=None, max_length=None, null=True, blank=True)
    auther = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    blog = models.TextField(null=True, blank=True)
    postdatetime = models.DateTimeField(null=True, blank=True)
    slug = AutoSlugField(populate_from='title',
                         null=True, blank=True)

    class Meta:
        ordering = ['id']
        
    def __str__(self):
        return str(self.title) 





    
   
class news_logo(models.Model):
    logo_img = models.ImageField(upload_to='logo_photos', height_field=None,
                                 width_field=None, max_length=None, null=True, blank=True)

    class Meta:
        verbose_name_plural = "News_Logo_img"
        db_table = 'news_logo_img'
