from django.db import models

class TestImage(models.Model):
    label = models.CharField(max_length=100, default='')
    image = models.CharField(max_length=100, default='ubuntu')
    tag   = models.CharField(max_length=100, default='recruit')