from django.db import models

# Create your models here.
from dvadmin.utils.models import CoreModel

class CrudSalinityModel(CoreModel):
    time = models.CharField(max_length=255, verbose_name="Time")
    salinity = models.FloatField(verbose_name="Salinity")

    class Meta:
        db_table = "Salinity"
        verbose_name = 'Salinity Table'
        verbose_name_plural = verbose_name
        # ordering = ('-create_datetime',)