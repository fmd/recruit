import string, random
from django.db import models
from recruit.tests.models import TestImage

class ApplicationManager(models.Manager):

    def pwgen(self):
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
        size = random.randint(8, 12)
        return ''.join(random.choice(chars) for x in range(size))

    def create_application(self, image, username, key):
        if self.filter(key=key).count() > 0:
            return self.get(key=key)

        a = self.create(username=username, password=self.pwgen(), test_image=TestImage.objects.get(image=image), key=key)
        return a

class Application(models.Model):
    objects    = ApplicationManager()
    test_image = models.ForeignKey(TestImage, related_name='tests', blank=True)
    container  = models.CharField(max_length=100, default='')
    username   = models.CharField(max_length=255, blank=True, default='')
    password   = models.CharField(max_length=255, blank=True, default='')
    key        = models.CharField(max_length=255, blank=True, default='')

    def __unicode__(self):
        return self.username

    def start(self):
        print "Starting container"