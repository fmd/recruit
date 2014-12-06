from django.db import models
from recruit.tests.models import TestImage

class Application(models.Model):
    test_image = models.ForeignKey(TestImage, related_name='tests')
    container  = models.CharField(max_length=100, default='')
    candidate  = models.CharField(max_length=255)