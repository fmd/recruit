from django.db import models
from recruit.tests.models import TestImage

class ApplicationManager(models.Manager):

    def pwgen(self):
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
        size = random.randint(8, 12)
        return ''.join(random.choice(chars) for x in range(size))

    def create_application(self, image, username, key):
        if self.get(key=key):
            return False

        a = self.create(username=username, password=self.pwgen(), test_image=TestImage.get(image=image), key=key)
        return a

class Application(models.Model):
    objects    = ApplicationManager
    test_image = models.ForeignKey(TestImage, related_name='tests', blank=True)
    container  = models.CharField(max_length=100, default='')
    candidate  = models.CharField(max_length=255, blank=True)
    username   = models.CharField(max_length=255, blank=True)
    password   = models.CharField(max_length=255, blank=True)
    key        = models.CharField(max_length=255, blank=True)

    def start(self):
        print "Starting container"