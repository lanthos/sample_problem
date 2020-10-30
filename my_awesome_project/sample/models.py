from django.db import models


class SampleModel(models.Model):
    is_working = models.BooleanField()
