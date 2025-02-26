from django.db import models


class TaskModel(models.Model):

    name = models.CharField(max_length=250, verbose_name="Имя")
    description = models.CharField(max_length=2000, verbose_name="Описание")
    is_done = models.BooleanField(default=False)
    priority = models.CharField(max_length=250, default="Средний", verbose_name="Приоритет")
