from django.db import models

# Create your models here.
from dvadmin.utils.models import CoreModel

class CrudPHModel(CoreModel):
    time = models.CharField(max_length=255, verbose_name="Time")
    ph = models.FloatField(verbose_name="PH")

    class Meta:
        db_table = "PH"
        verbose_name = 'PH Table'
        verbose_name_plural = verbose_name
        # ordering = ('-create_datetime',)