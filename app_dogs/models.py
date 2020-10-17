from django.db import models
from django.contrib.auth.models import User
from softdelete.models import SoftDeleteObject


class Dogs(SoftDeleteObject, models.Model):
    name = models.CharField(max_length=150, verbose_name='кличка', db_index=True)
    birthday = models.DateField(verbose_name='дата рождения')
    arrived_at = models.DateField(verbose_name='дата прибытия')
    weight = models.FloatField(verbose_name='вес')
    height = models.FloatField(verbose_name='рост')
    special = models.TextField(max_length=1000, verbose_name='особые приметы')
    shelter = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='название приюта', blank=True, null=True)

    def __str__(self):
        return self.name
