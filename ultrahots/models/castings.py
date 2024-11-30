from django.db import models

class CarMake(models.Model):
    name = models.CharField(max_length=255)

class Casting(models.Model):
    make = models.ForeignKey(
        'CarMake',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    name = models.CharField(max_length=255)


class Release(models.Model):
    year = models.IntegerField()

    collector_number = models.CharField(max_length=255, blank=True, default='')
    toy_number = models.CharField(max_length=255, blank=True, default='')

    casting = models.ForeignKey(
        'Casting',
        on_delete=models.CASCADE
    )
    
    color = models.CharField(max_length=255)

    # base_color 
    # base_type (i.e. plastic, metal)
    # window_tint
    # interior color
    # notes (json? text?)
    # country
    # photo