from django.db import models

# Create your models here.


class contact_us_logo(models.Model):
    logo_img = models.ImageField(upload_to='logo_photos', height_field=None,
                                 width_field=None, max_length=None, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Contact_Logo_img"
        db_table = 'Contact_logo_img'


class Contact_Us(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=50)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "Contact_By_User"
        db_table = 'Contact_By_User'
