from django.db import models
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create your models here.
superpower_choices = (
    ('Volar', 'Volar'),
    ('Superinteligencia', 'Superinteligencia'),
    ('Vista de rayo láser', 'Vista de rayo láser'),
    ('Billetera gorda', 'Billetera gorda'),
)


hero_choices = (
   ('Heroe', 'Heroe/Heroina'),
   ('Villano', 'Villano/Villana')
)


class Superheroe(models.Model):
    name = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    profile_image = models.ImageField(null=True, blank=True, upload_to="images/")
    superpower = models.CharField(choices=superpower_choices, max_length=19, null=False, blank=False, default=None)
    heroe_villano = models.CharField(choices=hero_choices, max_length=15, null=False, blank=False, default=None)
    description = RichTextField(blank=True, null=True)
    date = models.DateField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #PARA VOLVER A HOME
        return reverse('home')