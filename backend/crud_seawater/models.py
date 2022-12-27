from django.db import models

# Create your models here.
from dvadmin.utils.models import CoreModel

class CrudSeawaterModel(CoreModel):
    time = models.CharField(max_length=255, verbose_name="Time")
    seawater = models.FloatField(verbose_name="Sea Water")

    class Meta:
        db_table = "Seawater"
        verbose_name = 'Seawater Table'
        verbose_name_plural = verbose_name
        # ordering = ('-create_datetime',)