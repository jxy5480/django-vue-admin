from django.db import models

# Create your models here.
from dvadmin.utils.models import CoreModel


class CrudDissolvedOxygenModel(CoreModel):
    time = models.CharField(max_length=255, verbose_name="Time")
    dissolved_oxygen = models.FloatField(verbose_name="Dissolved Oxygen")

    class Meta:
        db_table = "dissolved_oxygen"
        verbose_name = 'Dissolved Oxygen Table'
        verbose_name_plural = verbose_name
        # ordering = ('-create_datetime',)